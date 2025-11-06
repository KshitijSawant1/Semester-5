import java.io.*; import java.net.*;

public class Client {
  public static void main(String[] a) throws Exception {
    try (Socket s=new Socket("localhost",5002);
         BufferedReader srv=new BufferedReader(new InputStreamReader(s.getInputStream()));
         PrintWriter out=new PrintWriter(s.getOutputStream(),true);
         BufferedReader kb=new BufferedReader(new InputStreamReader(System.in))) {

      new Thread(() -> {  // reader
        try { for (String r; (r=srv.readLine())!=null; ) System.out.println(r); }
        catch (IOException ignored) {}
        System.out.println("Disconnected."); System.exit(0);
      }).start();

      for (String line; (line=kb.readLine())!=null; ) {
        out.println(line);
        if ("/exit".equalsIgnoreCase(line)) break;
      }
    }
  }
}
