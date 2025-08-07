import java.math.BigInteger;
class Solution {
    public String addBinary(String a, String b) {
        BigInteger aBig = new BigInteger(a,2);
        BigInteger bBig = new BigInteger(b,2);
        aBig = aBig.add(bBig);
        return aBig.toString(2);
    }
}