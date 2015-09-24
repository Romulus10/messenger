package JMessageServer;

import java.io.IOException;
import java.net.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class JMessageServer {

    static ServerSocket sock;

    public static void main(String[] args) {
        try {
            sock = new ServerSocket(1551);
        } catch (IOException ex) {
            Logger.getLogger(JMessageServer.class.getName()).log(Level.SEVERE, null, ex);
        }

        try {
            Socket serviceSocket = sock.accept();
        } catch (IOException ex) {
            Logger.getLogger(JMessageServer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
