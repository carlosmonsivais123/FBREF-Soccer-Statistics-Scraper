import scrapy
from scrapy.http import Request
import pandas as pd
import numpy as np

class messi_page_scraper(scrapy.Spider):
    name = 'messi'

    start_urls = ['https://fbref.com/en/players/d70ce98e/all_comps/Lionel-Messi-Stats---All-Competitions']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'messi.csv',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        base_url = "https://fbref.com"
        seasons  = response.css("a[href*= '/summary/Lionel-Messi-Match-Logs']")
        links = seasons.css("a::attr(href)").extract()[0:17]

        i = 0
        while i < len(links):
            for link in links:
                recipelink = "https://fbref.com" + link
                yield response.follow(link, callback = self.parse_following_urls)
                i = i + 1

    def parse_following_urls(self, response):
        data = response.css("table[id = 'matchlogs_all']>tbody>tr")

        dates = []
        for row in data:
            date_ind = row.css("th>a[href*= '/en/matches/']::text").extract()
            if len(date_ind) == 0:
                dates.append(["None"])
            else:
                dates.append(date_ind)

        day_of_the_week = []
        for row in data:
            day_of_the_week_ind = row.css("td[data-stat='dayofweek']::text").extract()
            if len(day_of_the_week_ind) == 0:
                day_of_the_week.append(["None"])
            else:
                day_of_the_week.append(day_of_the_week_ind)

        competition = []
        for row in data:
            competition_ind = row.css("td[data-stat='comp']>a::text").extract()
            if len(competition_ind) == 0:
                competition.append(["None"])
            else:
                competition.append(competition_ind)

        round = []
        for row in data:
            round_ind = row.css("td[data-stat='round']>a::text").extract()
            if len(round_ind) == 0:
                round.append(["None"])
            else:
                round.append(round_ind)

        venue = []
        for row in data:
            venue_ind = row.css("td[data-stat='venue']::text").extract()
            if len(venue_ind) == 0:
                venue.append(["None"])
            else:
                venue.append(venue_ind)

        result = []
        for row in data:
            result_ind = row.css("td[data-stat='result']::text").extract()
            if len(result_ind) == 0:
                result.append(["None"])
            else:
                result.append(result_ind)

        squad = []
        for row in data:
            squad_ind = row.css("td[data-stat='squad']>a::text").extract()
            if len(squad_ind) == 0:
                squad.append(["None"])
            else:
                squad.append(squad_ind)

        opponent = []
        for row in data:
            opponent_ind = row.css("td[data-stat='opponent']>a::text").extract()
            if len(opponent_ind) == 0:
                opponent.append(["None"])
            else:
                opponent.append(opponent_ind)

        game_started = []
        for row in data:
            game_started_ind = row.css("td[data-stat='game_started']::text").extract()
            if len(game_started_ind) == 0:
                game_started.append(["None"])
            else:
                game_started.append(game_started_ind)

        position = []
        for row in data:
            position_ind = row.css("td[data-stat='position']::text").extract()
            if len(position_ind) == 0:
                position.append(["None"])
            else:
                position.append(position_ind)

        minutes = []
        for row in data:
            minutes_ind = row.css("td[data-stat='minutes']::text").extract()
            if len(minutes_ind) == 0:
                minutes.append(["None"])
            else:
                minutes.append(minutes_ind)

        goals = []
        for row in data:
            goals_ind = row.css("td[data-stat='goals']::text").extract()
            if len(goals_ind) == 0:
                goals.append(["None"])
            else:
                goals.append(goals_ind)

        assists = []
        for row in data:
            assists_ind = row.css("td[data-stat='assists']::text").extract()
            if len(assists_ind) == 0:
                assists.append(["None"])
            else:
                assists.append(assists_ind)

        pens_made = []
        for row in data:
            pens_made_ind = row.css("td[data-stat='pens_made']::text").extract()
            if len(pens_made_ind) == 0:
                pens_made.append(["None"])
            else:
                pens_made.append(pens_made_ind)

        pens_att = []
        for row in data:
            pens_att_ind = row.css("td[data-stat='pens_att']::text").extract()
            if len(pens_att_ind) == 0:
                pens_att.append(["None"])
            else:
                pens_att.append(pens_att_ind)

        shots_total = []
        for row in data:
            shots_total_ind = row.css("td[data-stat='shots_total']::text").extract()
            if len(shots_total_ind) == 0:
                shots_total.append(["None"])
            else:
                shots_total.append(shots_total_ind)

        shots_on_target = []
        for row in data:
            shots_on_target_ind = row.css("td[data-stat='shots_on_target']::text").extract()
            if len(shots_on_target_ind) == 0:
                shots_on_target.append(["None"])
            else:
                shots_on_target.append(shots_on_target_ind)

        cards_yellow = []
        for row in data:
            cards_yellow_ind = row.css("td[data-stat='cards_yellow']::text").extract()
            if len(cards_yellow_ind) == 0:
                cards_yellow.append(["None"])
            else:
                cards_yellow.append(cards_yellow_ind)

        cards_red = []
        for row in data:
            cards_red_ind = row.css("td[data-stat='cards_red']::text").extract()
            if len(cards_red_ind) == 0:
                cards_red.append(["None"])
            else:
                cards_red.append(cards_red_ind)

        fouls = []
        for row in data:
            fouls_ind = row.css("td[data-stat='fouls']::text").extract()
            if len(fouls_ind) == 0:
                fouls.append(["None"])
            else:
                fouls.append(fouls_ind)

        fouled = []
        for row in data:
            fouled_ind = row.css("td[data-stat='fouled']::text").extract()
            if len(fouled_ind) == 0:
                fouled.append(["None"])
            else:
                fouled.append(fouled_ind)

        offsides = []
        for row in data:
            offsides_ind = row.css("td[data-stat='offsides']::text").extract()
            if len(offsides_ind) == 0:
                offsides.append(["None"])
            else:
                offsides.append(offsides_ind)

        crosses = []
        for row in data:
            crosses_ind = row.css("td[data-stat='crosses']::text").extract()
            if len(crosses_ind) == 0:
                crosses.append(["None"])
            else:
                crosses.append(crosses_ind)

        tackles_won = []
        for row in data:
            tackles_won_ind = row.css("td[data-stat='tackles_won']::text").extract()
            if len(tackles_won_ind) == 0:
                tackles_won.append(["None"])
            else:
                tackles_won.append(tackles_won_ind)

        interceptions = []
        for row in data:
            interceptions_ind = row.css("td[data-stat='interceptions']::text").extract()
            if len(interceptions_ind) == 0:
                interceptions.append(["None"])
            else:
                interceptions.append(interceptions_ind)

        own_goals = []
        for row in data:
            own_goals_ind = row.css("td[data-stat='own_goals']::text").extract()
            if len(own_goals_ind) == 0:
                own_goals.append(["None"])
            else:
                own_goals.append(own_goals_ind)

        pens_won = []
        for row in data:
            pens_won_ind = row.css("td[data-stat='pens_won']::text").extract()
            if len(pens_won_ind) == 0:
                pens_won.append(["None"])
            else:
                pens_won.append(pens_won_ind)

        pens_conceded = []
        for row in data:
            pens_conceded_ind = row.css("td[data-stat='pens_conceded']::text").extract()
            if len(pens_conceded_ind) == 0:
                pens_conceded.append(["None"])
            else:
                pens_conceded.append(pens_conceded_ind)

        touches = []
        for row in data:
            touches_ind = row.css("td[data-stat='touches']::text").extract()
            if len(touches_ind) == 0:
                touches.append(["None"])
            else:
                touches.append(touches_ind)

        pressure = []
        for row in data:
            pressure_ind = row.css("td[data-stat='pressures']::text").extract()
            if len(pressure_ind) == 0:
                pressure.append(["None"])
            else:
                pressure.append(pressure_ind)


        tackle = []
        for row in data:
            tackle_ind = row.css("td[data-stat='tackles']::text").extract()
            if len(tackle_ind) == 0:
                tackle.append(["None"])
            else:
                tackle.append(tackle_ind)

        interceptions = []
        for row in data:
            interceptions_ind = row.css("td[data-stat='interceptions']::text").extract()
            if len(interceptions_ind) == 0:
                interceptions.append(["None"])
            else:
                interceptions.append(interceptions_ind)

        blocks = []
        for row in data:
            blocks_ind = row.css("td[data-stat='blocks']::text").extract()
            if len(blocks_ind) == 0:
                blocks.append(["None"])
            else:
                blocks.append(blocks_ind)

        sca = []
        for row in data:
            sca_ind = row.css("td[data-stat='sca']::text").extract()
            if len(sca_ind) == 0:
                sca.append(["None"])
            else:
                sca.append(sca_ind)

        gca = []
        for row in data:
            gca_ind = row.css("td[data-stat='gca']::text").extract()
            if len(gca_ind) == 0:
                gca.append(["None"])
            else:
                gca.append(gca_ind)

        passes_completed = []
        for row in data:
            passes_completed_ind = row.css("td[data-stat='passes_completed']::text").extract()
            if len(passes_completed_ind) == 0:
                passes_completed.append(["None"])
            else:
                passes_completed.append(passes_completed_ind)

        passes_attempted = []
        for row in data:
            passes_attempted_ind = row.css("td[data-stat='passes']::text").extract()
            if len(passes_attempted_ind) == 0:
                passes_attempted.append(["None"])
            else:
                passes_attempted.append(passes_attempted_ind)

        ppd = []
        for row in data:
            ppd_ind = row.css("td[data-stat='passes_progressive_distance']::text").extract()
            if len(ppd_ind) == 0:
                ppd.append(["None"])
            else:
                ppd.append(ppd_ind)

        carries = []
        for row in data:
            carries_ind = row.css("td[data-stat='carries']::text").extract()
            if len(carries_ind) == 0:
                carries.append(["None"])
            else:
                carries.append(carries_ind)

        carries_distance = []
        for row in data:
            carries_distance_ind = row.css("td[data-stat='carry_progressive_distance']::text").extract()
            if len(carries_distance_ind) == 0:
                carries_distance.append(["None"])
            else:
                carries_distance.append(carries_distance_ind)

        succesful_dribbles = []
        for row in data:
            succesful_dribbles_ind = row.css("td[data-stat='dribbles_completed']::text").extract()
            if len(succesful_dribbles_ind) == 0:
                succesful_dribbles.append(["None"])
            else:
                succesful_dribbles.append(succesful_dribbles_ind)

        dribbles_attempted = []
        for row in data:
            dribbles_attempted_ind = row.css("td[data-stat='dribbles']::text").extract()
            if len(dribbles_attempted_ind) == 0:
                dribbles_attempted.append(["None"])
            else:
                dribbles_attempted.append(dribbles_attempted_ind)

        yield {"Dates": dates,
               "Day of the Week": day_of_the_week,
               "Competition": competition,
               "Round": round,
               "Venue": venue,
               "Result": result,
               "Squad": squad,
               "Opponent": opponent,
               "Game Started": game_started,
               "Position": position,
               "Minutes": minutes,
               "Goals": goals,
               "Assists": assists,
               "Pens Made": pens_made,
               "Pens Att": pens_att,
               "Shots Total": shots_total,
               "Shots on Target": shots_on_target,
               "Yellow Cards": cards_yellow,
               "Red Cards": cards_red,
               "Fouls": fouls,
               "Fouled": fouled,
               "Offsides": offsides,
               "Crosses": crosses,
               "Tackles Won": tackles_won,
               "Interceptions": interceptions,
               "Own Goals": own_goals,
               "Penalties Won": pens_won,
               "Penalties Conceded": pens_conceded,
               "Touches": touches,
               "Pressures": pressure,
               "Tackles": tackle,
               "Interceptions": interceptions,
               "Blocks": blocks,
               "Shot Creating Actions": sca,
               "Goal Creating Actions": gca,
               "Passes Completed": passes_completed,
               "Passes Attempted": passes_attempted,
               "Passes Progressive Distance": ppd,
               "Carries": carries,
               "Carries Distance": carries_distance,
               "Successful Dribbles": succesful_dribbles,
               "Dribble Attempted": dribbles_attempted
               }
