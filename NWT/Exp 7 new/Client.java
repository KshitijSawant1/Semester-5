import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 5002);
        System.out.println("Connected to server.");

        BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        String message;
        while (true) {
            System.out.print("Enter message (type 'exit' to quit): ");
            message = userInput.readLine();
            out.println(message);
            if (message.equalsIgnoreCase("exit")) break;
        }

        socket.close();
    }
}
