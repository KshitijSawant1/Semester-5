import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket ss = new ServerSocket(5002);
        System.out.println("Server waiting...");
        Socket s = ss.accept();
        System.out.println("Client connected.");

        BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
        String msg;
        while ((msg = in.readLine()) != null && !msg.equalsIgnoreCase("exit"))
            System.out.println("Client: " + msg);

        s.close();
        ss.close();
    }
}
