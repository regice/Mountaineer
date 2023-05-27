
# Mountaineer

Single-page site listing new operators to headhunting and recruitment, rewards, and other updates for upcoming Arknights events (based on the CN server). Named after Mountain from Arknights.

Data source: [Gamepress](https://gamepress.gg/arknights/) and the [Arknights Fandom Wiki](https://arknights.fandom.com/wiki/Arknights_Wiki)

# How It Works
Mountaineer is written with Python in conjunction with Flask and Bootstrap. It is deployed via Heroku. 

Since I have limited experience with backend engineering, I opted to use Python dictionaries and JSON files to store the data for the website. Likewise, I feel more comfortable using Python than Javascript (didn't get past tutorial hell; that's for another day), so Flask and Bootstrap allowed me to more easily get this site up and going.

# Considerations / To-do List
- Light theme - I decided on a(n ugly) darker color scheme because I prefer dark themes, but truthfully, a light theme with this color palette would look much better aesthetically. I wanted to stick with this color palette because it's color-picked from a reference picture of Mountain.
- Dictionary vs Database - Currently, all of the data for the website is split between a bunch of JSON files, and it's a bit of a headache to manage a bunch of dictionaries when making any changes. I might switch to a database design one day, but again, I'm not that skilled and knowledgeable with backend engineering so it would have taken me much longer to get this website going. As such, I'm not sure about how I would address any changes that I want to make to the database. Would I have to delete everything? Backend is another area that I want to dive into eventually.
