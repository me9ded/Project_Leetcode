int compare(const void *a,const void *b){
    return(*(int*)b-*(int*)a);
}
int numRescueBoats(int* people, int peopleSize, int limit) {
    qsort(people,peopleSize,sizeof(int),compare);
    int l=0;
    int r=peopleSize-1;
    while(l<=r){
        if(people[l]+people[r]<=limit){
            r-=1;
        }
        l+=1;
    }
    return l;
}