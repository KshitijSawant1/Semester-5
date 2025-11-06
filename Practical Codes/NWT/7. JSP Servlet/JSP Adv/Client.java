import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        Socket s = new Socket("localhost", 5002);
        System.out.println("Connected to server.");
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(s.getOutputStream(), true);

        String msg;
        while (!(msg = in.readLine()).equalsIgnoreCase("exit"))
            out.println(msg);

        s.close();
    }
}
