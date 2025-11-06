import java.io.*;
import java.net.*;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class Server {
    private static final int PORT = 5002;
    private static final List<ClientHandler> clients = new CopyOnWriteArrayList<>();

    public static void main(String[] args) throws IOException {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Server running on port " + PORT);

            // Console sender: type messages on server to broadcast to all clients
            Thread console = new Thread(() -> {
                try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
                    String line;
                    while ((line = br.readLine()) != null) {
                        if ("/exit".equalsIgnoreCase(line)) break;
                        broadcast("[Server] " + line);
                    }
                } catch (IOException ignored) {}
                System.out.println("Server console stopped.");
            });
            console.setDaemon(true);
            console.start();

            // Accept loop
            while (true) {
                Socket s = ss.accept();
                ClientHandler h = new ClientHandler(s);
                clients.add(h);
                new Thread(h).start();
            }
        }
    }

    static void broadcast(String msg) {
        for (ClientHandler c : clients) c.send(msg);
        System.out.println(msg);
    }

    static class ClientHandler implements Runnable {
        private final Socket socket;
        private PrintWriter out;
        private BufferedReader in;
        private String name = "User";

        ClientHandler(Socket s) { this.socket = s; }

        public void run() {
            try (socket) {
                in  = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);

                out.println("Welcome! Enter your name:");
                String maybeName = in.readLine();
                if (maybeName != null && !maybeName.isBlank()) name = maybeName.trim();

                broadcast("[Join] " + name + " connected.");

                String line;
                while ((line = in.readLine()) != null) {
                    if ("/exit".equalsIgnoreCase(line)) break;
                    broadcast(name + ": " + line);
                }
            } catch (IOException ignored) {
            } finally {
                clients.remove(this);
                broadcast("[Leave] " + name + " disconnected.");
            }
        }

        void send(String msg) { if (out != null) out.println(msg); }
    }
}
