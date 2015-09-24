package jmessage;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Listener extends Thread {

    private Socket socket;
    DataInputStream input;

    @Override
    public void run() {
        //System.out.println("Listener initialized.");
        try {
            Resources.serve = new ServerSocket(5441);
        } catch (IOException ex) {
            Logger.getLogger(Listener.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            socket = Resources.serve.accept();
        } catch (IOException ex) {
            Logger.getLogger(Listener.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            input = new DataInputStream(socket.getInputStream());
        } catch (IOException e) {
            System.out.println(e);
        }

        while (true) {
            try {
                String message = input.readLine();
                System.out.println(Resources.en.decode(message));
            } catch (IOException ex) {
                Logger.getLogger(Listener.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}
