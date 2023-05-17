-- 12-no_genre.sql
-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT t.title, g.genre_id
	FROM tv_shows as t
		LEFT JOIN tv_show_genres as g
		ON t.id = g.show_id
		WHERE g.genre_id IS NULL
	ORDER BY t.title, g.genre_id;
