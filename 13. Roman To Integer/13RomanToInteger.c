int romanToInt(char * s){

    // num will save the charater vaule, ans the total value of the roman number
    int num, ans = 0;

    // For each character in the string, counting from the end
    for(int i = strlen(s) - 1; i >= 0; i--)
    {
        // We get the value of the character
        switch(s[i])
        {
           case 'I' : num = 1; break;
           case 'V' : num = 5; break;
           case 'X' : num = 10; break;
           case 'L' : num = 50; break;
           case 'C' : num = 100; break;
           case 'D' : num = 500; break;
           case 'M' : num = 1000; break;
        }
        
        // And for every exception like IV, IX, XL, XC, CD, CM, where the value of the character is less than the value 
        // of the next character, we need to subtract the value of the character to the answer
        if (4*num < ans)
        {
            ans -= num;
        } else {
            ans += num;
        }
    }
    
    return ans;
}