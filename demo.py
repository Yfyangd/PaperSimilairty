#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TextSimilarity(object):
    
    def __init__(self,file_a,file_b):

        str_a = ''
        str_b = ''
        if not os.path.isfile(file_a):
            print(file_a,"is not file")
            return
        elif not os.path.isfile(file_b):
            print(file_b,"is not file")
            return
        else:
            with open(file_a,'r', encoding='UTF-8') as f:
                for line in f.readlines():
                    str_a += line.strip()
                
                f.close()
            with open(file_b,'r', encoding='UTF-8') as f:
                for line in f.readlines():
                    str_b += line.strip()
                
                f.close()
        
        self.str_a = str_a
        self.str_b = str_b
            

    def splitWords(self,str_a):
        wordsa=pseg.cut(str_a)
        cuta = ""
        seta = set()
        for key in wordsa:
            cuta += key.word + " "
            seta.add(key.word)
        
        return [cuta, seta]
    
    def JaccardSim(self,str_a,str_b):
        seta = self.splitWords(str_a)[1]
        setb = self.splitWords(str_b)[1]
        sa_sb = 1.0 * len(seta & setb) / len(seta | setb)

        return sa_sb
    
    
    def countIDF(self,text,topK):
        tfidf = analyse.extract_tags
        cipin = {}
        fenci = jieba.cut(text)

        for word in fenci:
            if word not in cipin.keys():
                cipin[word] = 0
            cipin[word] += 1

        keywords = tfidf(text,topK,withWeight=True)

        ans = []
        for keyword in keywords:
            ans.append(cipin[keyword[0]])
        return ans

    def cos_sim(a,b):
        a = np.array(a)
        b = np.array(b)
        return np.sum(a*b) / (np.sqrt(np.sum(a ** 2)) * np.sqrt(np.sum(b ** 2)))
    
    def pers_sim(a,b):
        a = np.array(a)
        b = np.array(b)

        a = a - np.average(a)
        b = b - np.average(b)

        return np.sum(a*b) / (np.sqrt(np.sum(a ** 2)) * np.sqrt(np.sum(b ** 2)))

    def splitWordSimlaryty(self,str_a,str_b,topK = 20,sim =cos_sim):
        vec_a = self.countIDF(str_a,topK)
        vec_b = self.countIDF(str_b,topK)
        
        return sim(vec_a,vec_b)

