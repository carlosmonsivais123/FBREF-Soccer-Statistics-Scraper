import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def clean_files(file_names):

    file_name = pd.read_csv("{}".format(file_names))

    dates_list = []
    for date in file_name["Dates"]:
        new_date = eval(date)
        new_date = [item for sublist in new_date for item in sublist]
        dates_list.append(new_date)
    dates_list = [item for sublist in dates_list for item in sublist]

    dow_list = []
    for day in file_name["Day of the Week"]:
        new_dow = eval(day)
        new_dow = [item for sublist in new_dow for item in sublist]
        dow_list.append(new_dow)
    dow_list = [item for sublist in dow_list for item in sublist]

    comp_list = []
    for comp in file_name["Competition"]:
        new_comp = eval(comp)
        new_comp = [item for sublist in new_comp for item in sublist]
        comp_list.append(new_comp)
    comp_list = [item for sublist in comp_list for item in sublist]

    round_list = []
    for rounder in file_name["Round"]:
        new_rounder = eval(rounder)
        new_rounder = [item for sublist in new_rounder for item in sublist]
        round_list.append(new_rounder)
    round_list = [item for sublist in round_list for item in sublist]

    venue_list = []
    for venue in file_name["Venue"]:
        new_venue = eval(venue)
        new_venue = [item for sublist in new_venue for item in sublist]
        venue_list.append(new_venue)
    venue_list = [item for sublist in venue_list for item in sublist]

    result_list = []
    for result in file_name["Result"]:
        new_result = eval(result)
        new_result = [item for sublist in new_result for item in sublist]
        result_list.append(new_result)
    result_list = [item for sublist in result_list for item in sublist]

    squad_list = []
    for squad in file_name["Squad"]:
        new_squad = eval(squad)
        new_squad = [item for sublist in new_squad for item in sublist]
        squad_list.append(new_squad)
    squad_list = [item for sublist in squad_list for item in sublist]

    opponent_list = []
    for opponent in file_name["Opponent"]:
        new_opponent = eval(opponent)
        new_opponent = [item for sublist in new_opponent for item in sublist]
        opponent_list.append(new_opponent)
    opponent_list = [item for sublist in opponent_list for item in sublist]

    game_started_list = []
    for game in file_name["Game Started"]:
        new_game_started = eval(game)
        new_game_started = [item for sublist in new_game_started for item in sublist]
        game_started_list.append(new_game_started)
    game_started_list = [item for sublist in game_started_list for item in sublist]

    position_list = []
    for position in file_name["Position"]:
        new_position = eval(position)
        new_position = [item for sublist in new_position for item in sublist]
        position_list.append(new_position)
    position_list = [item for sublist in position_list for item in sublist]

    minutes_list = []
    for minutes in file_name["Minutes"]:
        new_minutes = eval(minutes)
        new_minutes = [item for sublist in new_minutes for item in sublist]
        minutes_list.append(new_minutes)
    minutes_list = [item for sublist in minutes_list for item in sublist]

    goals_list = []
    for goals in file_name["Goals"]:
        new_goals = eval(goals)
        new_goals = [item for sublist in new_goals for item in sublist]
        goals_list.append(new_goals)
    goals_list = [item for sublist in goals_list for item in sublist]

    assists_list = []
    for assists in file_name["Assists"]:
        new_assists = eval(assists)
        new_assists = [item for sublist in new_assists for item in sublist]
        assists_list.append(new_assists)
    assists_list = [item for sublist in assists_list for item in sublist]

    pens_made_list = []
    for pens_made in file_name["Pens Made"]:
        new_pens_made = eval(pens_made)
        new_pens_made = [item for sublist in new_pens_made for item in sublist]
        pens_made_list.append(new_pens_made)
    pens_made_list = [item for sublist in pens_made_list for item in sublist]

    pens_att_list = []
    for pens_att in file_name["Pens Att"]:
        new_pens_att = eval(pens_att)
        new_pens_att = [item for sublist in new_pens_att for item in sublist]
        pens_att_list.append(new_pens_att)
    pens_att_list = [item for sublist in pens_att_list for item in sublist]

    shots_total_list = []
    for shots_tot in file_name["Shots Total"]:
        new_shots_total = eval(shots_tot)
        new_shots_total = [item for sublist in new_shots_total for item in sublist]
        shots_total_list.append(new_shots_total)
    shots_total_list = [item for sublist in shots_total_list for item in sublist]

    shots_target_list = []
    for shots_target in file_name["Shots on Target"]:
        new_shots_target = eval(shots_target)
        new_shots_target = [item for sublist in new_shots_target for item in sublist]
        shots_target_list.append(new_shots_target)
    shots_target_list = [item for sublist in shots_target_list for item in sublist]

    yellow_cards_list = []
    for yellow_cards in file_name["Yellow Cards"]:
        new_yellow_cards = eval(yellow_cards)
        new_yellow_cards = [item for sublist in new_yellow_cards for item in sublist]
        yellow_cards_list.append(new_yellow_cards)
    yellow_cards_list = [item for sublist in yellow_cards_list for item in sublist]

    red_cards_list = []
    for red_cards in file_name["Red Cards"]:
        new_red_cards = eval(red_cards)
        new_red_cards = [item for sublist in new_red_cards for item in sublist]
        red_cards_list.append(new_red_cards)
    red_cards_list = [item for sublist in red_cards_list for item in sublist]

    fouls_list = []
    for fouls in file_name["Fouls"]:
        new_fouls = eval(fouls)
        new_fouls = [item for sublist in new_fouls for item in sublist]
        fouls_list.append(new_fouls)
    fouls_list = [item for sublist in fouls_list for item in sublist]

    fouled_list = []
    for fouled in file_name["Fouled"]:
        new_fouled = eval(fouled)
        new_fouled = [item for sublist in new_fouled for item in sublist]
        fouled_list.append(new_fouled)
    fouled_list = [item for sublist in fouled_list for item in sublist]

    offsides_list = []
    for offsides in file_name["Offsides"]:
        new_offsides = eval(offsides)
        new_offsides = [item for sublist in new_offsides for item in sublist]
        offsides_list.append(new_offsides)
    offsides_list = [item for sublist in offsides_list for item in sublist]

    crosses_list = []
    for crosses in file_name["Crosses"]:
        new_crosses = eval(crosses)
        new_crosses = [item for sublist in new_crosses for item in sublist]
        crosses_list.append(new_crosses)
    crosses_list = [item for sublist in crosses_list for item in sublist]

    tackles_won_list = []
    for tackles in file_name["Tackles Won"]:
        new_tackles_won = eval(tackles)
        new_tackles_won = [item for sublist in new_tackles_won for item in sublist]
        tackles_won_list.append(new_tackles_won)
    tackles_won_list = [item for sublist in tackles_won_list for item in sublist]

    interceptions_list = []
    for interceptions in file_name["Interceptions"]:
        new_interceptions = eval(interceptions)
        new_interceptions = [item for sublist in new_interceptions for item in sublist]
        interceptions_list.append(new_interceptions)
    interceptions_list = [item for sublist in interceptions_list for item in sublist]

    own_goals_list = []
    for own_goals in file_name["Own Goals"]:
        new_own_goals = eval(own_goals)
        new_own_goals = [item for sublist in new_own_goals for item in sublist]
        own_goals_list.append(new_own_goals)
    own_goals_list = [item for sublist in own_goals_list for item in sublist]

    penalties_won_list = []
    for penalties_won in file_name["Penalties Won"]:
        new_penalties_won = eval(penalties_won)
        new_penalties_won = [item for sublist in new_penalties_won for item in sublist]
        penalties_won_list.append(new_penalties_won)
    penalties_won_list = [item for sublist in penalties_won_list for item in sublist]

    penalties_conceded_list = []
    for penalties_conceded in file_name["Penalties Conceded"]:
        new_penalties_conceded = eval(penalties_conceded)
        new_penalties_conceded = [item for sublist in new_penalties_conceded for item in sublist]
        penalties_conceded_list.append(new_penalties_conceded)
    penalties_conceded_list = [item for sublist in penalties_conceded_list for item in sublist]

    touches_list = []
    for touches in file_name["Touches"]:
        new_touches = eval(touches)
        new_touches = [item for sublist in new_touches for item in sublist]
        touches_list.append(new_touches)
    touches_list = [item for sublist in touches_list for item in sublist]

    pressure_list = []
    for pressure in file_name["Pressures"]:
        new_pressure = eval(pressure)
        new_pressure = [item for sublist in new_pressure for item in sublist]
        pressure_list.append(new_pressure)
    pressure_list = [item for sublist in pressure_list for item in sublist]

    tackles_list = []
    for tackles in file_name["Tackles"]:
        new_tackles = eval(tackles)
        new_tackles = [item for sublist in new_tackles for item in sublist]
        tackles_list.append(new_tackles)
    tackles_list = [item for sublist in tackles_list for item in sublist]

    blocks_list = []
    for blocks in file_name["Blocks"]:
        new_blocks = eval(blocks)
        new_blocks = [item for sublist in new_blocks for item in sublist]
        blocks_list.append(new_blocks)
    blocks_list = [item for sublist in blocks_list for item in sublist]

    shot_creating_actions_list = []
    for sca in file_name["Shot Creating Actions"]:
        new_shot_creating_actions = eval(sca)
        new_shot_creating_actions = [item for sublist in new_shot_creating_actions for item in sublist]
        shot_creating_actions_list.append(new_shot_creating_actions)
    shot_creating_actions_list = [item for sublist in shot_creating_actions_list for item in sublist]

    goal_creating_actions_list = []
    for gca in file_name["Goal Creating Actions"]:
        new_goal_creating_actions = eval(gca)
        new_goal_creating_actions = [item for sublist in new_goal_creating_actions for item in sublist]
        goal_creating_actions_list.append(new_goal_creating_actions)
    goal_creating_actions_list = [item for sublist in goal_creating_actions_list for item in sublist]

    passes_completed_list = []
    for passes_completed in file_name["Passes Completed"]:
        new_passes_completed = eval(passes_completed)
        new_passes_completed = [item for sublist in new_passes_completed for item in sublist]
        passes_completed_list.append(new_passes_completed)
    passes_completed_list = [item for sublist in passes_completed_list for item in sublist]

    passes_attempted_list = []
    for passes_attempted in file_name["Passes Attempted"]:
        new_passes_attempted = eval(passes_attempted)
        new_passes_attempted = [item for sublist in new_passes_attempted for item in sublist]
        passes_attempted_list.append(new_passes_attempted)
    passes_attempted_list = [item for sublist in passes_attempted_list for item in sublist]

    ppd_list = []
    for ppd in file_name["Passes Progressive Distance"]:
        new_ppd_list = eval(ppd)
        new_ppd_list = [item for sublist in new_ppd_list for item in sublist]
        ppd_list.append(new_ppd_list)
    ppd_list = [item for sublist in ppd_list for item in sublist]

    carries_list = []
    for carries in file_name["Carries"]:
        new_carries_list = eval(carries)
        new_carries_list = [item for sublist in new_carries_list for item in sublist]
        carries_list.append(new_carries_list)
    carries_list = [item for sublist in carries_list for item in sublist]

    carries_distance_list = []
    for carries_distance in file_name["Carries Distance"]:
        new_carries_distance_list = eval(carries_distance)
        new_carries_distance_list = [item for sublist in new_carries_distance_list for item in sublist]
        carries_distance_list.append(new_carries_distance_list)
    carries_distance_list = [item for sublist in carries_distance_list for item in sublist]

    successful_dribbles_list = []
    for successful_dribbles in file_name["Successful Dribbles"]:
        new_successful_dribbles_list = eval(successful_dribbles)
        new_successful_dribbles_list = [item for sublist in new_successful_dribbles_list for item in sublist]
        successful_dribbles_list.append(new_successful_dribbles_list)
    successful_dribbles_list = [item for sublist in successful_dribbles_list for item in sublist]

    dribble_attempted_list = []
    for dribble_attempted in file_name["Dribble Attempted"]:
        new_dribble_attempted_list = eval(dribble_attempted)
        new_dribble_attempted_list = [item for sublist in new_dribble_attempted_list for item in sublist]
        dribble_attempted_list.append(new_dribble_attempted_list)
    dribble_attempted_list = [item for sublist in dribble_attempted_list for item in sublist]

    df = pd.DataFrame()
    df["Dates"] = dates_list

    ###################### Cleaning Results String ######################
    results = pd.DataFrame()
    results["Result"] = result_list
    string_length = []
    for string in results["Result"]:
        string_length.append(len(string))
    results["Length"] = string_length
    first_string = results[(results["Length"] == 4) & (results["Result"] != "None")]
    first = first_string["Result"].tolist()
    first_indexes = list(first_string.index)
    second_string = results[results["Length"] <= 3]
    second = second_string["Result"].tolist()
    second_indexes = list(second_string.index)
    i = 0
    new_string = []
    for value in first:
        new = value.rstrip() + second[i].rstrip()
        i = i + 1
        new_string.append(new)
    i = 0
    for value in first_indexes:
        results.loc[value, "Result"] = new_string[i]
        i = i + 1
    results.drop(results.index[second_indexes], inplace = True)
    results.reset_index(inplace = True, drop = True)
    results = pd.DataFrame(results["Result"])
    ################################################################
    df = pd.merge(df, results, left_index = True, right_index = True)

    df["Day of the Week"] = dow_list
    df["Competition"] = comp_list
    df["Round"] = round_list
    df["Venue"] = venue_list
    df["Squad"] = squad_list
    df["Opponent"] = opponent_list
    df["Game Started"] = game_started_list
    df["Minutes"] = minutes_list
    df["Goals"] = goals_list
    df["Assists"] = assists_list
    df["Pens Made"] = pens_made_list
    df["Pens Att"] = pens_att_list
    df["Shots Total"] = shots_total_list
    df["Shots on Target"] = shots_target_list
    df["Yellow Cards"] = yellow_cards_list
    df["Red Cards"] = red_cards_list
    df["Fouls"] = fouls_list
    df["Fouled"] = fouled_list
    df["Offsides"] = offsides_list
    df["Crosses"] = crosses_list
    df["Tackles Won"] = tackles_won_list
    df["Interceptions"] = interceptions_list
    df["Own Goals"] = own_goals_list
    df["Penalties Won"] = penalties_won_list
    df["Penalties Conceded"] = penalties_conceded_list
    df["Touches"] = touches_list
    df["Pressures"] = pressure_list
    df["Tackles"] = tackles_list
    df["Blocks"] = blocks_list
    df["Shot Creating Actions"] = shot_creating_actions_list
    df["Goal Creating Actions"] = goal_creating_actions_list
    df["Passes Completed"] = passes_completed_list
    df["Passes Attempted"] = passes_attempted_list
    df["Passes Progressive Distance"] = ppd_list
    df["Carries"] = carries_list
    df["Carries Distance"] = carries_distance_list
    df["Successful Dribbles"] = successful_dribbles_list
    df["Dribbles Attempted"] = dribble_attempted_list

    df = df[~df["Dates"].str.contains("None")]
    df['Dates'] = pd.to_datetime(df['Dates'], format="%Y/%m/%d")
    df['Dates'] = df['Dates'].dt.date

    df.reset_index(inplace = True, drop = True)
    df.sort_values(by = "Dates", inplace = True)
    df.reset_index(inplace = True, drop = True)

    df.replace(to_replace="None", value=np.nan, inplace=True)
    df["Minutes"].replace(to_replace=np.nan, value="0", inplace=True)
    df["Goals"].replace(to_replace=np.nan, value="0", inplace=True)
    df["Red Cards"].replace(to_replace=np.nan, value="0", inplace=True)
    df["Yellow Cards"].replace(to_replace=np.nan, value="0", inplace=True)
    df["Own Goals"].replace(to_replace=np.nan, value="0", inplace=True)
    df["Assists"].replace(to_replace=np.nan, value="0", inplace=True)

    df['Minutes'] = df['Minutes'].astype(float)
    df['Goals'] = df['Goals'].astype(float)
    df['Assists'] = df['Assists'].astype(float)
    df['Pens Made'] = df['Pens Made'].astype(float)
    df['Pens Att'] = df['Pens Att'].astype(float)
    df['Shots Total'] = df['Shots Total'].astype(float)
    df['Shots on Target'] = df['Shots on Target'].astype(float)
    df['Yellow Cards'] = df['Yellow Cards'].astype(float)
    df['Red Cards'] = df['Red Cards'].astype(float)
    df['Fouls'] = df['Fouls'].astype(float)
    df['Fouled'] = df['Fouled'].astype(float)
    df['Offsides'] = df['Offsides'].astype(float)
    df['Crosses'] = df['Crosses'].astype(float)
    df['Tackles Won'] = df['Tackles Won'].astype(float)
    df['Interceptions'] = df['Interceptions'].astype(float)
    df['Own Goals'] = df['Own Goals'].astype(float)
    df['Penalties Won'] = df['Penalties Won'].astype(float)
    df['Penalties Conceded'] = df['Penalties Conceded'].astype(float)
    df['Touches'] = df['Touches'].astype(float)
    df['Pressures'] = df['Pressures'].astype(float)
    df['Tackles'] = df['Tackles'].astype(float)
    df['Blocks'] = df['Blocks'].astype(float)
    df['Shot Creating Actions'] = df['Shot Creating Actions'].astype(float)
    df['Goal Creating Actions'] = df['Goal Creating Actions'].astype(float)
    df['Passes Completed'] = df['Passes Completed'].astype(float)
    df['Passes Attempted'] = df['Passes Attempted'].astype(float)
    df['Passes Progressive Distance'] = df['Passes Progressive Distance'].astype(float)
    df['Carries'] = df['Carries'].astype(float)
    df['Carries Distance'] = df['Carries Distance'].astype(float)
    df['Successful Dribbles'] = df['Successful Dribbles'].astype(float)
    df['Dribbles Attempted'] = df['Dribbles Attempted'].astype(float)

    win_draw_loss = []
    for value in df["Result"]:
        win_draw_loss.append(value[0])
    df["Win Draw Loss"] = win_draw_loss

    df["Cummulative Goals"] = df["Goals"].cumsum(axis = 0)

    general_comp = []
    for value in df["Competition"]:
        if value in ['La Liga', 'Primeira Liga', 'Premiership', 'Premier League', 'Serie A']:
            general_comp.append("League")
        elif value in ['Champions Lg', 'UEFA Cup']:
            general_comp.append("Champions League")
        elif value in ['Copa del Rey', 'Supercopa de España', 'Super Cup', 'Coppa Italia', 'Supercoppa Italiana']:
            general_comp.append("League Cups")
        elif value in ['Copa América', 'FIFA Confederations Cup', 'WCQ', 'Copa América Centenario', 'WCQ — UEFA (M)', 'UEFA Euro', 'Euro Qualifying', 'UEFA Nations League']:
            general_comp.append("International Tournaments")
        elif value in ['Friendlies (M)']:
            general_comp.append("Friendlies")
        elif value in ['FIFA World Cup']:
            general_comp.append("World Cup")
    df["General Competition"] = general_comp

    did_he_play = []
    for value in df["Minutes"]:
        if value > 0:
            did_he_play.append("Played")
        else:
            did_he_play.append("Not Played")
    df["Played"] = did_he_play

    i = 0
    games_no_goal = []
    for row in df["Goals"]:
        if row < 1:
            i = i + 1
            games_no_goal.append(i)
        else:
            i = 0
            games_no_goal.append(0)
    df["Games With no Goal"] = games_no_goal

    df = df[['Dates', 'Result', "Win Draw Loss", 'Day of the Week', 'Competition', "General Competition", 'Round', 'Venue',
             'Squad', 'Opponent', 'Game Started', 'Minutes', 'Played', 'Goals', "Cummulative Goals", 'Assists',
             'Pens Made', 'Pens Att', 'Shots Total', 'Shots on Target',
             'Yellow Cards', 'Red Cards', 'Interceptions', 'Own Goals',
             'Touches', 'Pressures', 'Shot Creating Actions', 'Goal Creating Actions',
             'Passes Completed', 'Passes Attempted', 'Passes Progressive Distance', 'Carries',
             'Carries Distance', 'Successful Dribbles', 'Dribbles Attempted', "Games With no Goal"]]


    # Need to change the Chile vs Argentina Result for the Copa America Final 2015 where Argentina lost 4-1 in penalties.
    # Need to change the Chile vs Argentina Result for the Copa America Final 2016 where Argentina lost 4-2 in penalties.
    if file_names=='messi.csv':
        df["Win Draw Loss"].iloc[483] = "L"
        df["Result"].iloc[483] = "L PEN(4–1)"

        df["Result"].iloc[542] = "L PEN(4–2)"

    else:
        pass

    # Need to change the Chelsea vs Manchester United Result for the Champions League Final 2008 where Manchester United won 6-5 in penalties.
    # Need to change the Atletico Madrid vs Realmadrid Result for the Champions League Final 2016 where Realmadrid won 5-3 in penalties.
    # Need to change the Juventus vs Napoli Result for the Coppa Italia Final 2020 where Juventus lost 4-2 in penalties.
    if file_names=='ronaldo.csv':
        df["Win Draw Loss"].iloc[280] = "W"
        df["Result"].iloc[280] = "W PEN(6–5)"

        df["Result"].iloc[695] = "W PEN(5–3)"

        df["Result"].iloc[896] = "L PEN(4–2)"

    else:
        pass

    name = file_names.split('.', 1)[0]

    df.to_excel("{} clean.xlsx".format(name), index = False)

clean_files("messi.csv")
clean_files("ronaldo.csv")
