def match_details(team1, team2):
    team1=team1.split()
    team1="".join(team1)
    team2=team2.split()
    team2="".join(team2)
    with open('matches.txt','r') as file:
        print(file.readline().strip())
        print(file.readline().strip())
        for line in file:
            x=line.split()
            if (team1==x[1] and team2==x[2]) or (team2==x[1] and team1==x[2]):
                print(line)


def remove_match(match_no):
    file=open('matches.txt','r')
    z=file.readlines()
    z=z[:match_no+1]+z[match_no+2:]
    Line=(z[match_no]).split()
    print(Line[-1])
    print(Line[-2])

    if Line[-1]!='TBG' or Line[-2]!='TBG':
        raise Exception('This match cannot be deleted')
    filelength=len(z)
    print(filelength)
    if match_no+2>filelength:
        raise Exception('No match of this number exists')
    x=match_no
    for i in range(x+1,filelength):
        line=z[i]
        w=str(i-1)+line[2:]
        z[i]=w
    file.close()
    file=open('matches.txt','w')
    file.writelines(z)
    file.close()
    print('Match record removed successfully')


def player_details(player_name):
    with open('players.txt','r') as file:
        print(file.readline())
        file.readline()
        lineNo=2
        for line in file:
            x=line.split()
            if player_name==x[0]:
                print(line)
                break
            lineNo +=1
   

def remove_player(player_name):
    with open('players.txt','r') as file:
        file.readline()
        file.readline()
        lineNo=2
        for line in file:
            x=line.split()
            if player_name==x[0]+" "+x[1]:
                break
            lineNo +=1
    with open('players.txt','r') as file:
        x=file.readlines()
        x=x[:lineNo]+x[lineNo+1:]
    with open('players.txt','w') as file:
        file.writelines(x)
    print('Player record removed successfully')


def add_player(name,team,age, bat, bowl,wk):
    with open('players.txt','a') as file:
        x=name.ljust(26)+team.ljust(16)+bat.ljust(9)+bowl.ljust(9)+wk.ljust(13)+str(age).ljust(5)
        file.write(x)
        
        
def main():
    remove_match(11)
main()