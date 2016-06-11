package jmessage;

import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Resources {

    public static Socket sock;
    public static Scanner scan = new Scanner(System.in);
    public static Encrypter en = new Encrypter(JMessage.key);
    public static Listener list = new Listener();
    public static ServerSocket serve;
    public static Sender send = new Sender();
}