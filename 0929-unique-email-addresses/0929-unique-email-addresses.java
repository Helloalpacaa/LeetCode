class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> uniqueEmails = new HashSet<>();
        for (String email: emails) {
            String formattedEmail = getFormattedEmail(email);
            uniqueEmails.add(formattedEmail);
        }
        return uniqueEmails.size();
    }
    
    private String getFormattedEmail (String email) {
        String[] arr = email.split("@");
        String localName = arr[0];
        String domainName = arr[1];
        
        String[] localNameWithPlus = localName.split("\\+");
        localName = localNameWithPlus[0];
        
        localName = localName.replace(".", "");
        
        return localName + "@" + domainName;
    }
}