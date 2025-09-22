import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5002);
        System.out.println("Server started. Waiting for client...");

        Socket socket = serverSocket.accept();
        System.out.println("Client connected.");

        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        String line;

        while ((line = in.readLine()) != null) {
            if (line.equalsIgnoreCase("exit")) break;
            System.out.println("Received from client: " + line);
        }

        socket.close();
        serverSocket.close();
    }
}
