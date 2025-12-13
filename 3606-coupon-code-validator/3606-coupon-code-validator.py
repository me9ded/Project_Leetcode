class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        number_of_coupons = len(code)
        result=[]
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        p_map= {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        for i in range(number_of_coupons):
            if (code[i].replace("_","").isalnum() or code[i]=='_') and businessLine[i] in categories and isActive[i] == True:
                result.append((code[i],businessLine[i]))
        result.sort(key=lambda x:(p_map[x[1]],x[0]))
        return [coupon for coupon,_ in result]