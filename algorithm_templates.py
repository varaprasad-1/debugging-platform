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

]