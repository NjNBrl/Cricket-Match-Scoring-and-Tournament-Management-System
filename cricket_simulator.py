import os
import random
import json
import math
#---------------------------------------------------------------------------------------------------
def pre_match(team1,team2,num_team1,num_team2):
    print("Toss winner will be randomly announced : ")
    x = random.randint(1,7)
    if (x % 2 == 0):
        print(f"{team1} won the toss")
        toss_winner = team1
        winners = num_team1
        toss_loser =  team2
        losers = num_team2
    else:
        print(f"{team2} won the toss")
        toss_winner = team2
        winners = num_team2
        toss_loser = team1
        losers = num_team1
    choice = int(input(f"\n1.BAT\n2.BOWL\n"))
    if choice == 1:
        print(f"{toss_winner} has decided to bat first")
        first_batting_team = toss_winner
        num_first_batting_team = winners
        first_bowling_team = toss_loser
        num_first_bowling_team = losers
    else:
        print(f"{toss_winner} has decided to bowl first")
        first_batting_team = toss_loser
        num_first_batting_team = losers
        first_bowling_team = toss_winner
        num_first_bowling_team = winners
    input("\nPress Enter to start the match...")

    os.system('cls' if os.name == 'nt' else 'clear')
    return first_batting_team, first_bowling_team, num_first_batting_team, num_first_bowling_team
#---------------------------------------------------------------------------------------------------
first_batters = []
def batting_stats_first(team_name,num_batting_team,batter_count):
    first_batters.append({
        "team_name" : team_name,
        "name" : input(f"Batter {num_batting_team - (num_batting_team-batter_count)} name: "),
        "runs" : 0,
        "balls" : 0,  
        "fours": 0,
        "sixes" : 0,
        "strike_rate" : 0.0,
        "bolden" : None,
        "lbw" : None,
        "stumped" : None,
        "runout" : None,
        "caught" : None,
        "retired" : None,
        "out_status": "Did not bat",
        "batter_count" : batter_count,
        "team_total" : 0,
        "wickets" : 0,
        "overs": 0.0

    })
#---------------------------------------------------------------------------------------------------
first_bowlers = []
def bowling_stats_first(team_name,bowler_count,bowler_id):
    first_bowlers.append({
        "team_name" : team_name,
        "name" : input(f"Bowler {bowler_count} name: "),
        "runs_given" : 0,
        "wickets_taken" : 0,
        "bowler_id": bowler_id,
        "current_bowler": 0,
        "overs" : 0.0
    })
#---------------------------------------------------------------------------------------------------
second_batters = []
def batting_stats_second(team_name,num_batting_team,batter_count):
    second_batters.append({
        "team_name" : team_name,
        "name" : input(f"Batter {num_batting_team - (num_batting_team-batter_count)} name: "),
        "runs" : 0,
        "balls" : 0,  
        "fours": 0,
        "sixes" : 0,
        "strike_rate" : 0.0,
        "bolden" : None,
        "lbw" : None,
        "stumped" : None,
        "runout" : None,
        "caught" : None,
        "retired" : None,
        "out_status": "Did not bat",
        "batter_count" : batter_count,
        "team_total" : 0,
        "wickets" : 0,
        "overs": 0.0
    })
#---------------------------------------------------------------------------------------------------
second_bowlers = []
def bowling_stats_second(team_name,bowler_count,bowler_id):
    second_bowlers.append({
        "team_name" : team_name,
        "name" : input(f"Bowler {bowler_count} name: "),
        "runs_given" : 0,
        "wickets_taken" : 0,
        "bowler_id": bowler_id,
        "current_bowler": 0,
        "overs" : 0.0
    })
#---------------------------------------------------------------------------------------------------
def first_innings(tournament_title,overs,batting_team,num_batting_team,bowling_team,num_bowling_team):
    retired_status = 0
    first_run_by_overs = [0]
    over = 0.0
    total_runs = 0
    wickets = 0
    batter_count = 1
    bowler_count = 1
    bowler_id = 0
    byes = 0
    wides = 0
    nb = 0
    lb = 0
    fall_of_wickets = []
    on_pitch = []
    batting_stats_first(batting_team,num_batting_team,batter_count)
    batter_count = batter_count + 1
    batting_stats_first(batting_team,num_batting_team,batter_count)
    strike = 0
    non_strike = 1
    first_batters[strike]["out_status"] = "not out"
    first_batters[non_strike]["out_status"] = "not out"
    on_pitch.append([strike,non_strike])
    partnership = [0]
    print("--------------------------------------------------------------------------------------------------------------------")
    while(over<overs and wickets < (num_batting_team-1)):

        current_over = 0.0
        bowling_stats_first(bowling_team,bowler_count,bowler_id)
        bowler_count = bowler_count + 1
        first_bowlers[bowler_id]["current_bowler"] = 1
        print("--------------------------------------------------------------------------------------------------------------------")
        print(f"Enter the event of the over : {over+1}")
        print(" Wd NB B LB Wkt 0 1 2 3 4 5 6 Retired")
        print("--------------------------------------------------------------------------------------------------------------------")
        for i in range(0,len(first_bowlers)-1):
            if first_bowlers[len(first_bowlers)-1]["name"] == first_bowlers[i]["name"]:
                first_bowlers[i]["current_bowler"] = 1 
                bowler_id = i
        j = 0
        while j < 6:
            print("***********************************************************************************************************************")
            print(f"\033[96m{batting_team} : {total_runs}/{wickets}                                       {over:.1f}\033[0m")
            print("--------------------------------------------------------------------------------------------------------------------")
            print(f"Stike : {first_batters[strike]["name"]}   {first_batters[strike]["runs"]}({first_batters[strike]["balls"]})*")
            print(f"Non-Stike : {first_batters[non_strike]["name"]}   {first_batters[non_strike]["runs"]}({first_batters[non_strike]["balls"]})*")
            print(f"Bowler : {first_bowlers[bowler_id]["name"]}  {first_bowlers[bowler_id]["wickets_taken"]}-{first_bowlers[bowler_id]["runs_given"]}")
            print("--------------------------------------------------------------------------------------------------------------------")
            over = over + 0.1
            current_over = current_over + 0.1
            event = input(f"{over:.1f} : ")
            if event == "Wd":
                j = j - 1
                over = over - 0.1
                wides = wides + 1
                print("Wideball")
                wide_runs = input("Any runs scored on a wide ball?(Y/N):")
                if wide_runs == "Y":
                    w_runs = int(input("Runs scored on wide ball : "))
                    if (w_runs % 2 == 1):
                        temp = strike
                        strike = non_strike
                        non_strike = temp
                    total_runs = total_runs + w_runs + 1
                    first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"]+ 1 + w_runs
                    byes = byes + w_runs
                else:
                    total_runs = total_runs + 1
                    first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"]+ 1
            elif event == "NB":
                j = j - 1
                print("No Ball, Free Hit")
                no_ball_runs = input("Any runs scored on no ball?(Y/N): ")
                if no_ball_runs == "Y":
                    n_run_type = input("Type of runs scored on no ball (1.Bye/2.Leg Bye/3.Legit Runs): ")
                    if n_run_type == "1":
                        n_runs = int(input("Runs scored on no ball : "))
                        if (n_runs % 2 == 1):
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                        total_runs = total_runs + n_runs + 1
                        first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"] + 1 + n_runs
                        byes = byes + n_runs
                    elif n_run_type == "2":
                        n_runs = int(input("Runs scored on no ball : "))
                        if (n_runs % 2 == 1):
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                        total_runs = total_runs + n_runs + 1
                        first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"] + 1 + n_runs
                        lb = lb + n_runs
                    else:
                        n_runs = int(input("Runs scored on no ball : "))
                        if (n_runs % 2 == 1):
                            first_batters[strike]["runs"] = first_batters[strike]["runs"] + n_runs
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                        else:
                            first_batters[strike]["runs"] = first_batters[strike]["runs"] + n_runs

                        total_runs = total_runs + n_runs + 1
                        first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"] + 1 + n_runs
                else:  
                    total_runs = total_runs + 1                   
                    first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"]+ 1
                over = over - 0.1
                nb = nb + 1

            elif event == "B":
                first_batters[strike]["balls"] = first_batters[strike]["balls"] + 1
                print("Bye")
                bye_runs = int(input("Bye runs : "))
                if (bye_runs % 2 == 1):
                    temp = strike
                    strike = non_strike
                    non_strike = temp
                total_runs = total_runs + bye_runs
                first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"]+ bye_runs
                byes = byes + bye_runs
            elif event == "LB":
                first_batters[strike]["balls"] = first_batters[strike]["balls"] + 1
                print("Leg Bye")
                leg_bye_runs = int(input("Leg Bye runs : "))
                if (leg_bye_runs % 2 == 1):
                    temp = strike
                    strike = non_strike
                    non_strike = temp
                total_runs = total_runs + leg_bye_runs
                first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"]+ leg_bye_runs
                lb = lb + leg_bye_runs
            elif event in ["0","1","2","3","4","5","6"]:
                runs_scored = int(event)
                first_batters[strike]["balls"] = first_batters[strike]["balls"] + 1
                if runs_scored == 4:
                    first_batters[strike]["fours"] = first_batters[strike]["fours"] + 1
                if runs_scored == 6:
                    first_batters[strike]["sixes"] = first_batters[strike]["sixes"] + 1
                if (runs_scored % 2 == 1):
                    first_batters[strike]["runs"] = first_batters[strike]["runs"] + runs_scored
                    temp = strike
                    strike = non_strike
                    non_strike = temp
                else:
                    first_batters[strike]["runs"] = first_batters[strike]["runs"] + runs_scored
                total_runs = total_runs + runs_scored
                first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"]+ runs_scored
            elif event == "Retired":
                j = j - 1
                over = over - 0.1
                num_batting_team = num_batting_team - 1
                retired_status = 1
    
                if wickets < (num_batting_team - 1):
                        batter_count += 1
                        
                    
                        print(f"Who was retired?\n 1.{first_batters[strike]["name"]} or 2.{first_batters[non_strike]["name"]}?")
                        retired = input("Enter 1/2 : ")
                        batting_stats_first(batting_team,num_batting_team, batter_count)

                        if strike>non_strike:
                            x = strike
                        else:
                            x = non_strike
                        if retired == "1":
                            first_batters[strike]["out_status"] = None
                            first_batters[strike]["retired"] = "Retired"
                            retired_strike = strike
                            strike = x + 1
                            first_batters[strike]["out_status"] = "not out"
                        else:
                            first_batters[non_strike]["out_status"] = None
                            first_batters[non_strike]["retired"] = "Retired"
                            retired_strike = non_strike
                            non_strike = x + 1
                            first_batters[non_strike]["out_status"] = "not out"
                        print(retired_strike)
                else:
                    print(f"Who was retired?\n 1.{first_batters[strike]["name"]} or 2.{first_batters[non_strike]["name"]}?")
                    retired = input("Enter 1/2 : ")
                    if retired == "1":
                            first_batters[strike]["out_status"] = None
                            first_batters[strike]["retired"] = "Retired"
                    else:
                            first_batters[non_strike]["out_status"] = None
                            first_batters[non_strike]["retired"] = "Retired"
                            
            elif event == "Wkt":
                first_batters[strike]["balls"] = first_batters[strike]["balls"] + 1

                print("Wicket")
                print("--------------------------------------------------------------------------------------------------------------------")
                fall_of_wickets.append(total_runs)
                partnership.append(total_runs)
                wickets = wickets + 1
                wicket_type  = input("Kind of wicket : \n1.Bowled \n2.Caught \n3.LBW \n4.Run Out \n5.Stumped\n")
                if wicket_type == "1":
                    print("Bowled")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_first(batting_team,num_batting_team, batter_count)
                        first_batters[strike]["bolden"] = " b " + first_bowlers[bowler_id]["name"]
                        if non_strike > strike:
                            first_batters[strike]["out_status"] = None
                            strike = non_strike + 1
                            first_batters[strike]["out_status"] = "not out"
                        else :
                            first_batters[strike]["out_status"] = None
                            strike = strike + 1
                            first_batters[strike]["out_status"] = "not out"
                        on_pitch.append([strike,non_strike])
                        first_bowlers[bowler_id]["wickets_taken"] = first_bowlers[bowler_id]["wickets_taken"] + 1
                    else:
                        first_batters[strike]["out_status"] = None
                        first_batters[strike]["bolden"] = " b " + first_bowlers[bowler_id]["name"]
                        first_bowlers[bowler_id]["wickets_taken"] = first_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            first_batters[retired_strike]["retired"] = None
                        else:
                            break
                    
                elif wicket_type == "2":
                    print("Caught")
                    caught_by = input("Caught by : ")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_first(batting_team,num_batting_team, batter_count)
                        first_batters[strike]["caught"] = " b " + first_bowlers[bowler_id]["name"] + "     c " + caught_by
                        if non_strike > strike:
                            first_batters[strike]["out_status"] = None
                            strike = non_strike + 1
                            first_batters[strike]["out_status"] = "not out"
                        else :
                            first_batters[strike]["out_status"] = None
                            strike = strike + 1
                            first_batters[strike]["out_status"] = "not out"
                        on_pitch.append([strike,non_strike])
                        first_bowlers[bowler_id]["wickets_taken"] = first_bowlers[bowler_id]["wickets_taken"] + 1
                        
                    else :
                        first_batters[strike]["out_status"] = None
                        first_batters[strike]["caught"] = " b " + first_bowlers[bowler_id]["name"] + "     c " + caught_by
                        first_bowlers[bowler_id]["wickets_taken"] = first_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            first_batters[retired_strike]["retired"] = None
                        else:
                            break
                elif wicket_type == "3":
                    print("LBW")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_first(batting_team,num_batting_team, batter_count)
                    else :
                        first_batters[strike]["out_status"] = None
                        first_batters[strike]["lbw"] = " lbw " + first_bowlers[bowler_id]["name"]
                        first_bowlers[bowler_id]["wickets_taken"] = first_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            first_batters[retired_strike]["retired"] = None
                        else:
                            break
                
                elif wicket_type == "5":
                    print("Stumped")
                    wicket_keeper = input("Wicket_keeper : ")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_first(batting_team,num_batting_team, batter_count)
                        first_batters[strike]["stumped"] = " b " + first_bowlers[bowler_id]["name"] + "     stmp " + wicket_keeper
                        if non_strike > strike:
                            first_batters[strike]["out_status"] = None
                            strike = non_strike + 1
                            first_batters[strike]["out_status"] = "not out"
                        else :
                            first_batters[strike]["out_status"] = None
                            strike = strike + 1
                            first_batters[strike]["out_status"] = "not out"
                        on_pitch.append([strike,non_strike])
                        first_bowlers[bowler_id]["wickets_taken"] = first_bowlers[bowler_id]["wickets_taken"] + 1
                    else :
                        first_batters[strike]["out_status"] = None
                        first_batters[strike]["stumped"] = " b " + first_bowlers[bowler_id]["name"] + "     stmp " + wicket_keeper
                        first_bowlers[bowler_id]["wickets_taken"] = first_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            first_batters[retired_strike]["retired"] = None
                        else:
                            break
                    
                elif wicket_type == "4":
                    print("Run Out")
                    runout_by = input(f"Run out by?")
                    print(f"Who was run out?\n 1.{first_batters[strike]["name"]} or 2.{first_batters[non_strike]["name"]}?")
                    run_out_strike = input("Enter 1/2 : ")
                    run_out_runs = int(input("Runs scored on run out: "))
                    first_bowlers[bowler_id]["runs_given"] = first_bowlers[bowler_id]["runs_given"] + run_out_runs
                    first_batters[strike]["runs"] = first_batters[strike]["runs"] + run_out_runs
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_first(batting_team,num_batting_team, batter_count)
                        if strike>non_strike:
                            x = strike
                        else:
                            x = non_strike
                        if run_out_strike == "1":
                            first_batters[strike]["runout"] = "Runout by " + runout_by
                            first_batters[strike]["out_status"] = None
                            strike = x + 1
                            first_batters[strike]["out_status"] = "not out"
                        else:
                            first_batters[non_strike]["runout"] = "Runout by" + runout_by
                            first_batters[non_strike]["out_status"] = None
                            non_strike = x + 1
                            first_batters[non_strike]["out_status"] = "not out"
                        print(f"Who should be on strike?1.{first_batters[strike]["name"]} or 2.{first_batters[non_strike]["name"]}" )
                        ans = input("1/2 : ")
                        if ans == 1:
                            break
                        else:
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                    else:
                        if run_out_strike == "1":
                            first_batters[strike]["runout"] = "Runout by" + runout_by
                            first_batters[strike]["out_status"] = None
                            flag = 100
                        else:
                            first_batters[non_strike]["runout"] = "Runout by" + runout_by
                            first_batters[non_strike]["out_status"] = None
                            non_strike = flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            first_batters[retired_strike]["retired"] = None
                        else:
                            break

                    on_pitch.append([strike,non_strike])
                    
                    first_bowlers[bowler_id]["overs"] = first_bowlers[bowler_id]["overs"] + over
            j = j + 1
        if current_over < 0.6:
            first_bowlers[bowler_id]["overs"] = current_over + first_bowlers[bowler_id]["overs"]
        else:    
            first_bowlers[bowler_id]["overs"] = 1.0 + first_bowlers[bowler_id]["overs"]
        if (wickets>=num_batting_team-1):
                over = int(over) + current_over
                break
        else: 
                over = 1.0 + int(over)
        bowler_id = first_bowlers[-1]["bowler_id"] + 1
        temp = strike
        strike = non_strike
        non_strike = temp
        print(f"*******************************************End of Over{over}****************************************************************************")
        print(f"\033[96m{batting_team} : {total_runs}/{wickets}                                       {over:.1f}\033[0m")
        print(f"Stike : {first_batters[strike]["name"]}   {first_batters[strike]["runs"]}({first_batters[strike]["balls"]})*")
        print(f"Non-Stike : {first_batters[non_strike]["name"]}   {first_batters[non_strike]["runs"]}({first_batters[non_strike]["balls"]})*")
        #--------------------------------------------------------------------------------------------------------------------------------------     
        #--------------------------------------------------------------------------------------------------------------------------------------
        first_run_by_overs.append(total_runs)
        input("\nNEXT....")
        os.system('cls' if os.name == 'nt' else 'clear')
    partnership.append(total_runs)
    input("\nPress Enter for scorecard...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"**************************************************BATTING SCORECARD {batting_team}***************************************************")
    for i in range(0,len(first_batters)):
        if first_batters[i]["balls"] == 0:
            print(f"{first_batters[i]["name"]}\t\t{first_batters[i]["runs"]}({first_batters[i]["balls"]})\t\t{first_batters[i]["runs"]*100/1:.1f}")
        else :
            print(f"{first_batters[i]["name"]}\t\t{first_batters[i]["runs"]}({first_batters[i]["balls"]})\t\t{first_batters[i]["runs"]*100/first_batters[i]["balls"]:.1f}")
        print(f"Fours : {first_batters[i]["fours"]}   Sixes : {first_batters[i]["sixes"]}")
        for key in ["bolden", "lbw", "stumped", "runout", "caught","out_status","retired"]:
            if first_batters[i][key] is not None:
                dismissal = first_batters[i][key]
                break

        print(dismissal)
        print("_______________________________________________________________________________________________________")
    print(f"EXTRAS :{wides+lb+byes+nb} ")
    print(f"{total_runs}/{wickets}\t{over:.1f}")
    input("\nPress Enter for bowling card...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"**************************************************BOWLING SCORECARD {bowling_team}***************************************************")
    for i in range(0,len(first_bowlers)):
        print(f"{first_bowlers[i]["name"]}\t\tOvers: {first_bowlers[i]["overs"]:.1f}\t\t Runs: {first_bowlers[i]["runs_given"]}\t\t Wickets: {first_bowlers[i]["wickets_taken"]}")
        print("_______________________________________________________________________________________________________")
    print("Fall of wickets : ")
    for index,item in enumerate(fall_of_wickets):
        print(f"{item} - {index+1}")
        
    input("\nPress Enter for partnership...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"**************************************************Partnership {batting_team}***************************************************")
    p_cal = 0
    for item in on_pitch:
        for p in range(1):
            pair = f"{first_batters[item[p]]['name']} and {first_batters[item[p+1]]['name']}"
            partnership_runs = partnership[p_cal+1] - partnership[p_cal]

            print(f"{pair:<40} {partnership_runs}")
        p_cal = p_cal + 1
    first_batters[0]["team_total"] = total_runs
    first_batters[0]["wickets"] = wickets
    first_batters[0]["overs"] = over
    if (wickets>=num_batting_team-1):
         first_run_by_overs.append(total_runs)
    with open(f"{tournament_title}/1.{batting_team}_batting.json","w") as file:
        json.dump(first_batters,file)
    with open(f"{tournament_title}/1.{bowling_team}_bowling.json","w") as file:
        json.dump(first_bowlers,file)
    return total_runs,wickets,over,first_run_by_overs
#---------------------------------------------------------------------------------------------------
def second_innings(tournament_title,target,overs,batting_team,num_batting_team,bowling_team,num_bowling_team):
    retired_status = 0
    second_run_by_overs = [0]
    over = 0.0
    total_runs = 0
    wickets = 0
    batter_count = 1
    bowler_count = 1
    bowler_id = 0
    byes = 0
    wides = 0
    nb = 0
    lb = 0
    fall_of_wickets = []
    on_pitch = []
    batting_stats_second(batting_team,num_batting_team,batter_count)
    batter_count = batter_count + 1
    batting_stats_second(batting_team,num_batting_team,batter_count)
    strike = 0
    non_strike = 1
    second_batters[strike]["out_status"] = "not out"
    second_batters[non_strike]["out_status"] = "not out"
    on_pitch.append([strike,non_strike])
    partnership = [0]
    print("--------------------------------------------------------------------------------------------------------------------")
    while(over<overs and wickets < (num_batting_team-1) and total_runs < target):

        current_over = 0.0
        bowling_stats_second(bowling_team,bowler_count,bowler_id)
        bowler_count = bowler_count + 1
        second_bowlers[bowler_id]["current_bowler"] = 1
        print("--------------------------------------------------------------------------------------------------------------------")
        print(f"Enter the event of the over : {over+1}")
        print(" Wd NB B LB Wkt 0 1 2 3 4 5 6 Retired")
        print("--------------------------------------------------------------------------------------------------------------------")
        for i in range(0,len(second_bowlers)-1):
            if second_bowlers[len(second_bowlers)-1]["name"] == second_bowlers[i]["name"]:
                second_bowlers[i]["current_bowler"] = 1 
                bowler_id = i
        j = 0
        while (j < 6 and total_runs<target):
            print("***********************************************************************************************************************")
            print(f"\033[96m{batting_team} : {total_runs}/{wickets}                                       {over:.1f}\033[0m")
            x = int((0.6-current_over)*10)
            if x == 0:
                y = 0
            if x == 6 :
                print(f"Need \033[92m{target - total_runs}\033[0m in \033[91m{int(overs - math.ceil(over))}.0\033[0m")
            else:
                print(f"Need \033[92m{target - total_runs}\033[0m in \033[91m{int(overs - math.ceil(over))}.{x}\033[0m")
            print("--------------------------------------------------------------------------------------------------------------------")
            print(f"Stike : {second_batters[strike]["name"]}   {second_batters[strike]["runs"]}({second_batters[strike]["balls"]})*")
            print(f"Non-Stike : {second_batters[non_strike]["name"]}   {second_batters[non_strike]["runs"]}({second_batters[non_strike]["balls"]})*")
            print(f"Bowler : {second_bowlers[bowler_id]["name"]}  {second_bowlers[bowler_id]["wickets_taken"]}-{second_bowlers[bowler_id]["runs_given"]}")
            print("--------------------------------------------------------------------------------------------------------------------")
            over = over + 0.1
            current_over = current_over + 0.1
            event = input(f"{over:.1f} : ")
            if event == "Wd":
                j = j - 1
                over = over - 0.1
                wides = wides + 1
                print("Wideball")
                wide_runs = input("Any runs scored on a wide ball?(Y/N):")
                if wide_runs == "Y":
                    w_runs = int(input("Runs scored on wide ball : "))
                    if (w_runs % 2 == 1):
                        temp = strike
                        strike = non_strike
                        non_strike = temp
                    total_runs = total_runs + w_runs + 1
                    second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"]+ 1 + w_runs
                    byes = byes + w_runs
                else:
                    total_runs = total_runs + 1
                    second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"]+ 1
            elif event == "NB":
                j = j - 1
                print("No Ball, Free Hit")
                no_ball_runs = input("Any runs scored on no ball?(Y/N): ")
                if no_ball_runs == "Y":
                    n_run_type = input("Type of runs scored on no ball (1.Bye/2.Leg Bye/3.Legit Runs): ")
                    if n_run_type == "1":
                        n_runs = int(input("Runs scored on no ball : "))
                        if (n_runs % 2 == 1):
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                        total_runs = total_runs + n_runs + 1
                        second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"] + 1 + n_runs
                        byes = byes + n_runs
                    elif n_run_type == "2":
                        n_runs = int(input("Runs scored on no ball : "))
                        if (n_runs % 2 == 1):
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                        total_runs = total_runs + n_runs + 1
                        second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"] + 1 + n_runs
                        lb = lb + n_runs
                    else:
                        n_runs = int(input("Runs scored on no ball : "))
                        if (n_runs % 2 == 1):
                            second_batters[strike]["runs"] = second_batters[strike]["runs"] + n_runs
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                        else:
                            second_batters[strike]["runs"] = second_batters[strike]["runs"] + n_runs

                        total_runs = total_runs + n_runs + 1
                        second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"] + 1 + n_runs
                else:  
                    total_runs = total_runs + 1                   
                    second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"]+ 1
                over = over - 0.1
                nb = nb + 1

            elif event == "B":
                second_batters[strike]["balls"] = second_batters[strike]["balls"] + 1
                print("Bye")
                bye_runs = int(input("Bye runs : "))
                if (bye_runs % 2 == 1):
                    temp = strike
                    strike = non_strike
                    non_strike = temp
                total_runs = total_runs + bye_runs
                second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"]+ bye_runs
                byes = byes + bye_runs
            elif event == "LB":
                second_batters[strike]["balls"] = second_batters[strike]["balls"] + 1
                print("Leg Bye")
                leg_bye_runs = int(input("Leg Bye runs : "))
                if (leg_bye_runs % 2 == 1):
                    temp = strike
                    strike = non_strike
                    non_strike = temp
                total_runs = total_runs + leg_bye_runs
                second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"]+ leg_bye_runs
                lb = lb + leg_bye_runs
            elif event in ["0","1","2","3","4","5","6"]:
                runs_scored = int(event)
                second_batters[strike]["balls"] = second_batters[strike]["balls"] + 1
                if runs_scored == 4:
                    second_batters[strike]["fours"] = second_batters[strike]["fours"] + 1
                if runs_scored == 6:
                    second_batters[strike]["sixes"] = second_batters[strike]["sixes"] + 1
                if (runs_scored % 2 == 1):
                    second_batters[strike]["runs"] = second_batters[strike]["runs"] + runs_scored
                    temp = strike
                    strike = non_strike
                    non_strike = temp
                else:
                    second_batters[strike]["runs"] = second_batters[strike]["runs"] + runs_scored
                total_runs = total_runs + runs_scored
                second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"]+ runs_scored
            elif event == "Retired":
                j = j - 1
                over = over - 0.1
                num_batting_team = num_batting_team - 1
                retired_status = 1
                if wickets < (num_batting_team - 1):
                        batter_count += 1
                    
                        print(f"Who was retired?\n 1.{second_batters[strike]["name"]} or 2.{second_batters[non_strike]["name"]}?")
                        retired = input("Enter 1/2 : ")
                        batting_stats_second(batting_team,num_batting_team, batter_count)

                        if strike>non_strike:
                            x = strike
                        else:
                            x = non_strike
                        if retired == "1":
                            second_batters[strike]["out_status"] = None
                            second_batters[strike]["retired"] = "Retired"
                            retired_strike = strike
                            strike = x + 1
                            second_batters[strike]["out_status"] = "not out"
                        else:
                            second_batters[non_strike]["out_status"] = None
                            second_batters[non_strike]["retired"] = "Retired"
                            retired_strike = non_strike
                            non_strike = x + 1
                            second_batters[non_strike]["out_status"] = "not out"
                else:
                    print(f"Who was retired?\n 1.{second_batters[strike]["name"]} or 2.{second_batters[non_strike]["name"]}?")
                    retired = input("Enter 1/2 : ")
                    if retired == "1":
                            second_batters[strike]["out_status"] = None
                            second_batters[strike]["retired"] = "Retired"
                    else:
                            second_batters[non_strike]["out_status"] = None
                            second_batters[non_strike]["retired"] = "Retired"
                    break
                            
            elif event == "Wkt":
                second_batters[strike]["balls"] = second_batters[strike]["balls"] + 1

                print("Wicket")
                print("--------------------------------------------------------------------------------------------------------------------")
                fall_of_wickets.append(total_runs)
                partnership.append(total_runs)
                wickets = wickets + 1
                wicket_type  = input("Kind of wicket : \n1.Bowled \n2.Caught \n3.LBW \n4.Run Out \n5.Stumped\n")
                if wicket_type == "1":
                    print("Bowled")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_second(batting_team,num_batting_team, batter_count)
                        second_batters[strike]["bolden"] = " b " + second_bowlers[bowler_id]["name"]
                        if non_strike > strike:
                            second_batters[strike]["out_status"] = None
                            strike = non_strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        else :
                            second_batters[strike]["out_status"] = None
                            strike = strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        on_pitch.append([strike,non_strike])
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                    else:
                        second_batters[strike]["out_status"] = None
                        second_batters[strike]["bolden"] = " b " + second_bowlers[bowler_id]["name"]
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            second_batters[retired_strike]["retired"] = None
                        else:
                            break
                    
                elif wicket_type == "2":
                    print("Caught")
                    caught_by = input("Caught by : ")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_second(batting_team,num_batting_team, batter_count)
                        second_batters[strike]["caught"] = " b " + second_bowlers[bowler_id]["name"] + "     c " + caught_by
                        if non_strike > strike:
                            second_batters[strike]["out_status"] = None
                            strike = non_strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        else :
                            second_batters[strike]["out_status"] = None
                            strike = strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        on_pitch.append([strike,non_strike])
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                    else :
                        second_batters[strike]["out_status"] = None
                        second_batters[strike]["caught"] = " b " + second_bowlers[bowler_id]["name"] + "     c " + caught_by
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            second_batters[retired_strike]["retired"] = None
                        else:
                            break
                elif wicket_type == "3":
                    print("LBW")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_second(batting_team,num_batting_team, batter_count)
                        second_batters[strike]["lbw"] = " lbw " + second_bowlers[bowler_id]["name"]
                        if non_strike > strike:
                            second_batters[strike]["out_status"] = None
                            strike = non_strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        else :
                            second_batters[strike]["out_status"] = None
                            strike = strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        on_pitch.append([strike,non_strike])
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                    else :
                        second_batters[strike]["out_status"] = None
                        second_batters[strike]["lbw"] = " lbw " + second_bowlers[bowler_id]["name"]
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            second_batters[retired_strike]["retired"] = None
                        else:
                            break
                    
                elif wicket_type == "5":
                    print("Stumped")
                    wicket_keeper = input("Wicket_keeper : ")
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_second(batting_team,num_batting_team, batter_count)
                        second_batters[strike]["stumped"] = " b " + second_bowlers[bowler_id]["name"] + "     stmp " + wicket_keeper
                        if non_strike > strike:
                            second_batters[strike]["out_status"] = None
                            strike = non_strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        else :
                            second_batters[strike]["out_status"] = None
                            strike = strike + 1
                            second_batters[strike]["out_status"] = "not out"
                        on_pitch.append([strike,non_strike])
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                    else :
                        second_batters[strike]["out_status"] = None
                        second_batters[strike]["stumped"] = " b " + second_bowlers[bowler_id]["name"] + "     stmp " + wicket_keeper
                        second_bowlers[bowler_id]["wickets_taken"] = second_bowlers[bowler_id]["wickets_taken"] + 1
                        flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            second_batters[retired_strike]["retired"] = None
                        else:
                            break
                elif wicket_type == "4":
                    print("Run Out")
                    runout_by = input(f"Run out by?")
                    print(f"Who was run out?\n 1.{second_batters[strike]["name"]} or 2.{second_batters[non_strike]["name"]}?")
                    run_out_strike = input("Enter 1/2 : ")
                    run_out_runs = int(input("Runs scored on run out: "))
                    second_bowlers[bowler_id]["runs_given"] = second_bowlers[bowler_id]["runs_given"] + run_out_runs
                    second_batters[strike]["runs"] = second_batters[strike]["runs"] + run_out_runs
                    if wickets < (num_batting_team - 1):
                        batter_count += 1
                        batting_stats_second(batting_team,num_batting_team, batter_count)
                        if strike>non_strike:
                            x = strike
                        else:
                            x = non_strike
                        if run_out_strike == "1":
                            second_batters[strike]["runout"] = "Runout by " + runout_by
                            second_batters[strike]["out_status"] = None
                            strike = x + 1
                            second_batters[strike]["out_status"] = "not out"
                        else:
                            second_batters[non_strike]["runout"] = "Runout by" + runout_by
                            second_batters[non_strike]["out_status"] = None
                            non_strike = x + 1
                            second_batters[non_strike]["out_status"] = "not out"
                        print(f"Who should be on strike?1.{second_batters[strike]["name"]} or 2.{second_batters[non_strike]["name"]}" )
                        ans = input("1/2 : ")
                        if ans == 1:
                            break
                        else:
                            temp = strike
                            strike = non_strike
                            non_strike = temp
                        on_pitch.append([strike,non_strike])
                    
                        second_bowlers[bowler_id]["overs"] = second_bowlers[bowler_id]["overs"] + over
                    else:
                        if run_out_strike == "1":
                            second_batters[strike]["runout"] = "Runout by" + runout_by
                            second_batters[strike]["out_status"] = None
                            flag = 100
                        else:
                            second_batters[non_strike]["runout"] = "Runout by" + runout_by
                            second_batters[non_strike]["out_status"] = None
                            non_strike = flag = 100
                        if ((wickets >= num_batting_team-1) and (retired_status == 1)):
                            question = input("Can the retired player play?(Y/N) : ")
                            if question == "Y":
                                if flag == 100:
                                        strike = retired_strike
                                else:
                                        non_strike = retired_strike
                            else:
                                 break
                            num_batting_team = num_batting_team + 1
                            retired_status = 0
                            second_batters[retired_strike]["retired"] = None
                        else:
                            break

            if (total_runs>=target) or (wickets>=num_batting_team-1):
                 second_run_by_overs.append(total_runs)        
            j = j + 1
        if current_over < 0.6:
            second_bowlers[bowler_id]["overs"] = current_over + second_bowlers[bowler_id]["overs"]
        else:    
            second_bowlers[bowler_id]["overs"] = 1.0 + second_bowlers[bowler_id]["overs"]
        if (wickets>=num_batting_team-1 or total_runs >=target):
                over = int(over) + current_over
                break
        else: 
                over = 1.0 + int(over)
        bowler_id = second_bowlers[-1]["bowler_id"] + 1
        temp = strike
        strike = non_strike
        non_strike = temp
        print(f"*******************************************End of Over{over}****************************************************************************")
        print(f"\033[96m{batting_team} : {total_runs}/{wickets}                                       {over:.1f}\033[0m")
        print(f"Stike : {second_batters[strike]["name"]}   {second_batters[strike]["runs"]}({second_batters[strike]["balls"]})*")
        print(f"Non-Stike : {second_batters[non_strike]["name"]}   {second_batters[non_strike]["runs"]}({second_batters[non_strike]["balls"]})*")
        #--------------------------------------------------------------------------------------------------------------------------------------     
        #--------------------------------------------------------------------------------------------------------------------------------------
        second_run_by_overs.append(total_runs)
        input("\nNEXT....")
        os.system('cls' if os.name == 'nt' else 'clear')
    partnership.append(total_runs)
    input("\nPress Enter for scorecard...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"**************************************************BATTING SCORECARD {batting_team}***************************************************")
    for i in range(0,len(second_batters)):
        if second_batters[i]["balls"] == 0:
            print(f"{second_batters[i]["name"]}\t\t{second_batters[i]["runs"]}({second_batters[i]["balls"]})\t\t{second_batters[i]["runs"]*100/1:.1f}")
        else :
            print(f"{second_batters[i]["name"]}\t\t{second_batters[i]["runs"]}({second_batters[i]["balls"]})\t\t{second_batters[i]["runs"]*100/second_batters[i]["balls"]:.1f}")
        print(f"Fours : {second_batters[i]["fours"]}   Sixes : {second_batters[i]["sixes"]}")
        for key in ["bolden", "lbw", "stumped", "runout", "caught","out_status","retired"]:
            if second_batters[i][key] is not None:
                dismissal = second_batters[i][key]
                break

        print(dismissal)
        print("_______________________________________________________________________________________________________")
    print(f"EXTRAS :{wides+lb+byes+nb} ")
    print(f"{total_runs}/{wickets}\t{over:.1f}")
    input("\nPress Enter for bowling card...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"**************************************************BOWLING SCORECARD {bowling_team}***************************************************")
    for i in range(0,len(second_bowlers)):
        print(f"{second_bowlers[i]["name"]}\t\tOvers: {second_bowlers[i]["overs"]:.1f}\t\t Runs: {second_bowlers[i]["runs_given"]}\t\t Wickets: {second_bowlers[i]["wickets_taken"]}")
        print("_______________________________________________________________________________________________________")
    print("Fall of wickets : ")
    for index,item in enumerate(fall_of_wickets):
        print(f"{item} - {index+1}")
        
    input("\nPress Enter for partnership...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"**************************************************Partnership {batting_team}***************************************************")
    p_cal = 0
    for item in on_pitch:
        for p in range(1):
            pair = f"{second_batters[item[p]]['name']} and {second_batters[item[p+1]]['name']}"
            partnership_runs = partnership[p_cal+1] - partnership[p_cal]

            print(f"{pair:<40} {partnership_runs}")
        p_cal = p_cal + 1
    second_batters[0]["team_total"] = total_runs
    second_batters[0]["wickets"] = wickets
    second_batters[0]["overs"] = over
    with open(f"{tournament_title}/2.{batting_team}_batting.json","w") as file:
        json.dump(second_batters,file)
    with open(f"{tournament_title}/2.{bowling_team}_bowling.json","w") as file:
        json.dump(second_bowlers,file)
    return total_runs,wickets,over,second_run_by_overs
#---------------------------------------------------------------------------------------------------
    
#---------------------------------------------------------------------------------------------------
def trend_lines(team, title, overs, i_overs,first_total_runs, first_wickets, first_over, first_run_by_overs):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mticker
    

    n = min(len(overs), len(first_run_by_overs))

    overs = overs[:n]
    first_run_by_overs = first_run_by_overs[:n]

    plt.plot(overs, first_run_by_overs, color="red")
    plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    plt.title(f"{title}\n{team} {first_total_runs}/{first_wickets} in {first_over:.1f}    ({i_overs})")
    plt.xlabel("Overs")
    plt.ylabel("Runs")

    plt.savefig(f"{team}_batting.png")
    plt.show()
#--------------------------------------------------------------------------------------------------
def trend_lines_both(teamA, teamB, title, overs, i_overs,
                     first_total_runs, first_wickets, first_over, first_run_by_overs,
                     second_total_runs, second_wickets, second_over, second_run_by_overs):

    import matplotlib.pyplot as plt
    import matplotlib.ticker as mticker

    n = min(len(overs), len(first_run_by_overs))
    m = min(len(overs), len(second_run_by_overs))

    f_overs = overs[:n]
    first_run_by_overs = first_run_by_overs[:n]

    s_overs = overs[:m]
    second_run_by_overs = second_run_by_overs[:m]
    plt.plot(f_overs, first_run_by_overs, color="red", label=teamA)
    plt.plot(s_overs, second_run_by_overs, color="blue", label=teamB)

    plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    plt.title(f"{title}\n"
              f"{teamA} {first_total_runs}/{first_wickets} in {first_over:.1f} ({i_overs})\n"
              f"{teamB} {second_total_runs}/{second_wickets} in {second_over:.1f} ({i_overs})")

    plt.xlabel("Overs")
    plt.ylabel("Runs")

    plt.legend()  # ✅ now works

    plt.savefig(f"{title}.png")
    plt.show()
#--------------------------------------------------------------------------------------------------
def over_calculation(historic_over,this_match_over):    
    o1 = int(historic_over)
    b1 = int(round((historic_over - o1) * 10))

    o2 = int(this_match_over)
    b2 = int(round((this_match_over - o2) * 10))

    # Normalize (handle cases like 2.6 → 3.0)
    o1 += b1 // 6
    b1 = b1 % 6

    o2 += b2 // 6
    b2 = b2 % 6

    # Add total balls
    total_balls = (o1 * 6 + b1) + (o2 * 6 + b2)

    return total_balls // 6 + (total_balls % 6) / 10

#--------------------------------------------------------------------------------------------------
def winner_announcement(tournament_title,num_first_bowling_team,
                        first_batting_team,
                        first_bowling_team,
                        first_total_runs,
                        first_wickets,
                        first_over,
                        second_total_runs,
                        second_wickets,
                        second_over,actual_first_over,actual_second_over):

    print(f"{first_batting_team}\t {first_total_runs}/{first_wickets}\t({actual_first_over:.1f})")
    print(f"{first_bowling_team}\t {second_total_runs}/{second_wickets}\t({actual_second_over:.1f})")

    if (second_total_runs > first_total_runs):
        print(f"{first_bowling_team} wins by {num_first_bowling_team-1-second_wickets} wicket(s)")
        winner = first_bowling_team
        loser = first_batting_team

    elif (second_total_runs < first_total_runs): 
        print(f"{first_batting_team} wins by {first_total_runs - second_total_runs} run(s)")
        winner = first_batting_team
        loser = first_bowling_team

    else:
        print("Tie, do a superover")
        return   # skip updating for tie (or handle separately)

    # --- LOAD JSON ---
    with open(f"{tournament_title}/points_table.json", "r") as f:
        table = json.load(f)

    # --- helper to find team ---
    def find_team(name):
        for team in table:
            if team["team_name"] == name:
                return team
        # if not found → create new
        new_team = {
            "team_name": name,
            "runs_for": 0,
            "overs_played": 0.0,
            "runs_against": 0,
            "overs_conceded": 0.0,
            "wins": 0,
            "loss": 0,
            "run_rate": 0.0
        }
        table.append(new_team)
        return new_team

    team1 = find_team(first_batting_team)
    team2 = find_team(first_bowling_team)

    # --- UPDATE BOTH TEAMS ---
    # batting team stats
    first_over_total_played = over_calculation(team1["overs_played"],first_over)
    f_o_t_p = int(first_over_total_played) + (first_over_total_played-int(first_over_total_played))/0.6
    first_over_total_conceded = over_calculation(team1["overs_conceded"],second_over)
    f_o_t_c = int(first_over_total_conceded) + (first_over_total_conceded-int(first_over_total_conceded))/0.6

    second_over_total_played = over_calculation(team2["overs_played"],second_over)
    s_o_t_p = int(second_over_total_played) + (second_over_total_played-int(second_over_total_played))/0.6
    second_over_total_conceded = over_calculation(team2["overs_conceded"],first_over)
    s_o_t_c = int(second_over_total_conceded) + (second_over_total_conceded-int(second_over_total_conceded))/0.6
    team1["runs_for"] += first_total_runs
    team1["overs_played"] = first_over_total_played
    team1["runs_against"] += second_total_runs
    team1["overs_conceded"] = first_over_total_conceded

    # bowling team stats
    team2["runs_for"] += second_total_runs
    team2["overs_played"] = second_over_total_played
    team2["runs_against"] += first_total_runs
    team2["overs_conceded"] = second_over_total_conceded
    
    # --- wins/loss ---
    if winner == first_batting_team:
        team1["wins"] += 1
        team2["loss"] += 1
    else:
        team2["wins"] += 1
        team1["loss"] += 1

    # --- RUN RATE (simple version, not perfect cricket math but fine) ---
    if team1["overs_played"] > 0:
        team1["run_rate"] = ((team1["runs_for"]) /f_o_t_p )-((team1["runs_against"] ) / f_o_t_c)

    if team2["overs_played"] > 0:
        team2["run_rate"] = ((team2["runs_for"] ) / s_o_t_p)-((team2["runs_against"]) / s_o_t_c)

    # --- SAVE BACK ---
    with open(f"{tournament_title}/points_table.json", "w") as f:
        json.dump(table, f, indent=4) 


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
tournament_title = input("Tournament name : (Else write FRIENDLY) ")
if not os.path.exists(tournament_title):
    os.mkdir(tournament_title)
title = input("Enter title of the match (eg: IPL MATCH 1 CSK V MI) : ")
team1 = input("Enter the first team: ")
num_team1 = int(input(f"Enter number of players in {team1}: "))
print()

team2 = input("Enter the second team: ")
num_team2 = int(input(f"Enter number of players in {team2}: "))
print()
overs = float(input("Enter the number of overs: "))
print()
over_list = [0]
i_overs = int(overs)
for i in range(0,i_overs):
    over_list.append(i+1)
input("\nPress Enter to start the toss")
os.system('cls' if os.name == 'nt' else 'clear')
#----------------------------------------------------------------------------------------------------
first_batting_team,first_bowling_team,num_first_batting_team,num_first_bowling_team = pre_match(team1, team2,num_team1,num_team2)
#----------------------------------------------------------------------------------------------------
first_total_runs,first_wickets,first_over,first_run_by_overs = first_innings(tournament_title,overs,first_batting_team,num_first_batting_team,first_bowling_team,num_first_bowling_team)
#----------------------------------------------------------------------------------------------------------------------------------------------
print("****************************************************************************************************")
trend_lines(first_batting_team,title,over_list,i_overs,first_total_runs,first_wickets,first_over,first_run_by_overs)
target = first_total_runs + 1
print(f"{first_batting_team} : {first_total_runs}/{first_wickets} ({first_over})")

print(f"{first_bowling_team} needs {target} runs to win in {overs} overs. RRR : {(target)/overs:.1f} ")
#---------------------------------------------------------------------------------------------------------------------------------
input("\nPress Enter to start second innings")
os.system('cls' if os.name == 'nt' else 'clear')
second_total_runs,second_wickets,second_over,second_run_by_overs = second_innings(tournament_title,target,overs,first_bowling_team,num_first_bowling_team,first_batting_team,num_first_batting_team)
actual_first_over = first_over
actual_second_over = second_over
input("\nPress Enter to proceed")
os.system('cls' if os.name == 'nt' else 'clear')
trend_lines_both(first_batting_team,first_bowling_team,title, over_list, i_overs,first_total_runs, first_wickets, first_over, first_run_by_overs,second_total_runs, second_wickets, second_over, second_run_by_overs)
if first_wickets == num_first_batting_team - 1:
     first_over = overs
if second_wickets == num_first_bowling_team - 1:
     second_over = overs
winner_announcement(tournament_title,num_first_bowling_team,first_batting_team,first_bowling_team,first_total_runs,first_wickets,first_over,second_total_runs,second_wickets,second_over,actual_first_over,actual_second_over)


