TEMPLATES = [

# ARRAY BASIC OPERATIONS

"""
int sum=0;
for(int i=0;i<n;i++){
    sum+=arr[i];
}
printf("%d",sum);
""",

"""
int max=arr[0];
for(int i=1;i<n;i++){
    if(arr[i]>max)
        max=arr[i];
}
printf("%d",max);
""",

"""
int min=arr[0];
for(int i=1;i<n;i++){
    if(arr[i]<min)
        min=arr[i];
}
printf("%d",min);
""",

"""
for(int i=0;i<n;i++){
    printf("%d",arr[i]);
}
""",

"""
for(int i=n-1;i>=0;i--){
    printf("%d",arr[i]);
}
""",

"""
int count=0;
for(int i=0;i<n;i++){
    if(arr[i]%2==0)
        count++;
}
printf("%d",count);
""",

"""
int count=0;
for(int i=0;i<n;i++){
    if(arr[i]%2!=0)
        count++;
}
printf("%d",count);
""",

"""
int product=1;
for(int i=0;i<n;i++){
    product*=arr[i];
}
printf("%d",product);
""",

"""
int avg=0;
for(int i=0;i<n;i++){
    avg+=arr[i];
}
avg/=n;
printf("%d",avg);
""",

"""
int sum=0;
for(int i=0;i<n;i++){
    if(arr[i]>0)
        sum+=arr[i];
}
printf("%d",sum);
""",

# SEARCHING

"""
int found=0;
for(int i=0;i<n;i++){
    if(arr[i]==target)
        found=1;
}
printf("%d",found);
""",

"""
int pos=-1;
for(int i=0;i<n;i++){
    if(arr[i]==target)
        pos=i;
}
printf("%d",pos);
""",

"""
int pos=-1;
for(int i=n-1;i>=0;i--){
    if(arr[i]==target)
        pos=i;
}
printf("%d",pos);
""",

# MATHEMATICAL

"""
int fact=1;
for(int i=1;i<=n;i++){
    fact*=i;
}
printf("%d",fact);
""",

"""
int sum=0;
for(int i=1;i<=n;i++){
    sum+=i;
}
printf("%d",sum);
""",

"""
int sum=0;
for(int i=1;i<=n;i++){
    if(i%2==0)
        sum+=i;
}
printf("%d",sum);
""",

"""
int sum=0;
for(int i=1;i<=n;i++){
    if(i%2!=0)
        sum+=i;
}
printf("%d",sum);
""",

"""
int count=0;
for(int i=1;i<=n;i++){
    if(n%i==0)
        count++;
}
printf("%d",count);
""",

"""
int flag=1;
for(int i=2;i<n;i++){
    if(n%i==0)
        flag=0;
}
printf("%d",flag);
""",

"""
int a=0,b=1,c;
for(int i=0;i<n;i++){
    c=a+b;
    a=b;
    b=c;
}
printf("%d",c);
""",

# STRING OPERATIONS

"""
for(int i=0;i<len;i++){
    printf("%c",str[i]);
}
""",

"""
for(int i=len-1;i>=0;i--){
    printf("%c",str[i]);
}
""",

"""
int count=0;
for(int i=0;i<len;i++){
    if(str[i]=='a')
        count++;
}
printf("%d",count);
""",

"""
int count=0;
for(int i=0;i<len;i++){
    if(str[i]==' ')
        count++;
}
printf("%d",count);
""",

# MATRIX OPERATIONS

"""
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        printf("%d",mat[i][j]);
    }
}
""",

"""
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        printf("%d",mat[j][i]);
    }
}
""",

"""
int sum=0;
for(int i=0;i<n;i++){
    sum+=mat[i][i];
}
printf("%d",sum);
""",

"""
int sum=0;
for(int i=0;i<n;i++){
    sum+=mat[i][n-i-1];
}
printf("%d",sum);
""",

"""
int sum=0;
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        sum+=mat[i][j];
    }
}
printf("%d",sum);
""",

# LOOP PATTERNS

"""
for(int i=1;i<=10;i++){
    printf("%d",i);
}
""",

"""
for(int i=10;i>=1;i--){
    printf("%d",i);
}
""",

"""
int i=0;
while(i<n){
    printf("%d",arr[i]);
    i++;
}
""",

"""
int i=0;
while(i<=n){
    printf("%d",arr[i]);
    i++;
}
""",

"""
int i=0;
do{
    printf("%d",i);
    i++;
}while(i<n);
""",

# SORTING ALGORITHMS

"""
for(int i=0;i<n-1;i++){
    for(int j=i+1;j<n;j++){
        if(arr[i]>arr[j]){
            int temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
        }
    }
}
""",

"""
for(int i=0;i<n-1;i++){
    for(int j=0;j<n-i-1;j++){
        if(arr[j]>arr[j+1]){
            int temp=arr[j];
            arr[j]=arr[j+1];
            arr[j+1]=temp;
        }
    }
}
""",

# SECOND LARGEST ELEMENT

"""
int first=arr[0],second=arr[1];
for(int i=2;i<n;i++){
    if(arr[i]>first){
        second=first;
        first=arr[i];
    }
}
printf("%d",second);
""",

# COUNT POSITIVE NUMBERS

"""
int count=0;
for(int i=0;i<n;i++){
    if(arr[i]>0)
        count++;
}
printf("%d",count);
""",

# COUNT NEGATIVE NUMBERS

"""
int count=0;
for(int i=0;i<n;i++){
    if(arr[i]<0)
        count++;
}
printf("%d",count);
""",

# SUM OF DIAGONAL MATRIX

"""
int sum=0;
for(int i=0;i<n;i++){
    sum+=mat[i][i];
}
printf("%d",sum);
""",

# PRINT MATRIX TRANSPOSE

"""
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        printf("%d",mat[j][i]);
    }
}
""",

# BINARY SEARCH STEP

"""
int low=0,high=n-1;
while(low<=high){
    int mid=(low+high)/2;
    if(arr[mid]==target)
        printf("Found");
    else if(arr[mid]<target)
        low=mid+1;
    else
        high=mid-1;
}
""",

# GCD OF TWO NUMBERS

"""
while(a!=b){
    if(a>b)
        a=a-b;
    else
        b=b-a;
}
printf("%d",a);
""",

# LCM OF TWO NUMBERS

"""
int max=(a>b)?a:b;
while(1){
    if(max%a==0 && max%b==0){
        printf("%d",max);
        break;
    }
    max++;
}
""",

# CHECK PALINDROME STRING

"""
int flag=1;
for(int i=0;i<len/2;i++){
    if(str[i]!=str[len-i-1])
        flag=0;
}
printf("%d",flag);
""",

# COUNT VOWELS

"""
int count=0;
for(int i=0;i<len;i++){
    if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
        count++;
}
printf("%d",count);
""",

# PRINT MULTIPLICATION TABLE

"""
for(int i=1;i<=10;i++){
    printf("%d",n*i);
}
""",

# SUM OF DIGITS

"""
int sum=0;
while(n>0){
    sum+=n%10;
    n=n/10;
}
printf("%d",sum);
""",

# REVERSE NUMBER

"""
int rev=0;
while(n>0){
    rev=rev*10+n%10;
    n=n/10;
}
printf("%d",rev);
""",

# COUNT DIGITS

"""
int count=0;
while(n>0){
    n=n/10;
    count++;
}
printf("%d",count);
""",

# POWER OF NUMBER

"""
int result=1;
for(int i=0;i<b;i++){
    result*=a;
}
printf("%d",result);
""",

# MATRIX ADDITION

"""
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        c[i][j]=a[i][j]+b[i][j];
    }
}
""",

# MATRIX SUBTRACTION

"""
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        c[i][j]=a[i][j]-b[i][j];
    }
}
""",

# COUNT ELEMENT GREATER THAN X

"""
int count=0;
for(int i=0;i<n;i++){
    if(arr[i]>x)
        count++;
}
printf("%d",count);
""",

# FIND SMALLEST POSITIVE NUMBER

"""
int min=arr[0];
for(int i=1;i<n;i++){
    if(arr[i]>0 && arr[i]<min)
        min=arr[i];
}
printf("%d",min);
""",
]