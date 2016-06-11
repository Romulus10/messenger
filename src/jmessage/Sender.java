package jmessage;

import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;

public class Sender {

    public void run() throws IOException {
        System.out.print("User name: ");
        String name = Resources.scan.nextLine();
        System.out.print("IP: ");
        String host = Resources.scan.nextLine();
        System.out.print("Key: ");
        Resources.en.key = Resources.scan.nextInt();
        Resources.sock = new Socket(host, 5441);
        PrintStream output;
        output = new PrintStream(Resources.sock.getOutputStream());
        output.println(Resources.en.encode(name + " has connected."));
        while (true) {
            String message = Resources.scan.nextLine();
            if ("quit".equals(message)) {
                System.exit(0);
            }
            message = name +  ": " + message;
            output.println(Resources.en.encode(message));
        }
    }
}
