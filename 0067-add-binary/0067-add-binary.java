import java.math.BigInteger;
class Solution {
    public String addBinary(String a, String b) {
        BigInteger aBig = new BigInteger(a,2);
        BigInteger bBig = new BigInteger(b,2);
        aBig = aBig.add(bBig);
        return aBig.toString(2);
        // long aVal = Long.parseLong(a,2), bVal = Long.parseLong(b,2);
        // long val = aVal + bVal;
        // String sol = Long.toBinaryString(val);
        // return sol;
    }
}