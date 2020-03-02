caesar = "Rpnd Yjaxd Rehpg, fjt th jcd st adh igth bah vgpcsth rpexipcth st ap Wxhidgxp rdc Patypcsgd Bpvcd n rdc Cpedatoc, th ipbqxec jcd st adh igth bah rdchxstgpqath wxhidgxpsdgth apixcdh, rdc Rpnd Rgxhed Hpajhixd n rdc Ixid Axkxd, udgbpcsd ta tytbeapg igxjckxgpid sta etgidsd raáhxrd edg tmrtatcrxp, etgidsd ktgspstgpbtcit «ajgtd» st aph atigph apixcph. Hx wph advgpsd aatvpg wphip pfji, ij gtrdbetchp htga ap st hpqtg fjt ap rdcigphtnp epgp hjetgpg thit gtid th Ratdepigp. N Yjaxd Rehpg th idsd thid, ixtct ipa hxvcxuxrprxoc, egtrxhpbtcit rdbd wxhidgxpsdg st hi bxhbd, cpggpsdg st hjh egdexph wpopnph vjtggtgph n st hj edaiixrp."

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

solution = ""
jump = 0

asciiList = [ord(c) for c in caesar]
abc = [ord(c) for c in abc]
ABC = [ord(c) for c in ABC]

while(jump < 26):
    newList = []
    for c in asciiList:
        if(c in abc):
            c = ((c + jump) - 97) % 26 + 97
            newList.append(c)
        elif(c in ABC):
            c = ((c + jump) - 65) % 26 + 65
            newList.append(c)
        else:
            newList.append(c)

    newList = [chr(c) for c in newList]
    solution = "".join(newList)
    
    print(solution)
    jump += 1

