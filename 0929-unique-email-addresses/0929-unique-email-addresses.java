class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> uniqueEmails = new HashSet<>();
        for (String email: emails) {
            String formattedEmail = formattedEmail(email);
            uniqueEmails.add(formattedEmail);
        }
        return uniqueEmails.size();
    }
    
    private String formattedEmail(String email) {
        // Split into localName and domainName
        String[] arr = email.split("@");
        String localName = arr[0];
        String domainName = arr[1];
        
        // Split localName if there is "+"
        String[] localNameWithPlus = localName.split("\\+");
        localName = localNameWithPlus[0];
        
        // Replace "." to ""
        localName = localName.replace(".", "");
        
        return localName + "@" + domainName;
    }
}