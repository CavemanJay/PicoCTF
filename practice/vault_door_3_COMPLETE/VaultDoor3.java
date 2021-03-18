import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = "picoCTF{abcdefghijklmnopqrstuvwxyz123456}"; // scanner.next();
        String input = userInput.substring("picoCTF{".length(), userInput.length() - 1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        int inputLength = password.length();
        if (inputLength != 32) {
            return false;
        }
        // String s = createEncryptedString(password);
        String encryptedPassword = "jU5t_a_sna_3lpm17ga45_u_4_mbrf4c";
        String decrypted = decryptPassword(encryptedPassword);
        System.out.println("picoCTF{" + decrypted + "}");

        // return decrypted.equals(encryptedPassword);
        return true;
    }

    public String decryptPassword(String password) {
        var indexOffsets = getOffsets();
        String decrypted = "";

        for (int i = 0; i < password.length(); i++) {
            int offset = indexOffsets.get(i);
            // char currentChar = password.charAt(i);
            // char offsetChar = (char) (currentChar - offset);
            char offsetChar = password.charAt(i - offset);
            decrypted += offsetChar;
        }

        return decrypted;
    }

    private ArrayList<Integer> getOffsets() {
        String original = "abcdefghijklmnopqrstuvwxyz123456";
        String encrypted = createEncryptedString(original);

        ArrayList<Integer> offsets = new ArrayList<>();
        for (char c : encrypted.toCharArray()) {
            // int index = encrypted.indexOf(Character.toString(c));
            // char matching = original.charAt(index);
            // int difference = c - matching;
            int encryptedIndex = encrypted.indexOf(Character.toString(c));
            int originalIndex = original.indexOf(Character.toString(c));
            int difference = encryptedIndex - originalIndex;

            offsets.add(difference);
        }

        return offsets;
    }

    private String createEncryptedString(String password) {
        char[] buffer = new char[32];
        int i;
        for (i = 0; i < 8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i < 16; i++) {
            buffer[i] = password.charAt(23 - i);
        }
        for (; i < 32; i += 2) {
            buffer[i] = password.charAt(46 - i);
        }
        for (i = 31; i >= 17; i -= 2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s;
    }
}
