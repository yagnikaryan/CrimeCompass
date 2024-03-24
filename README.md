# CrimeCompass
# Inspiration
Our inspiration for Crime Compass came from a conversation with a friend who felt unsafe and anxious blindly following a GPS when walking, especially in areas she was new and unfamiliar with. We saw that while there are many navigation tools available, few prioritize the user's safety regarding crime. Understanding that this was probably an issue experienced by many, we were motivated to create a solution that not only guides individuals to their destinations but also ensures their journey avoids areas with high crime rates. The idea was to blend technology with data analytics to make everyday travel safer for everyone.

# What it does
Crime Compass is a navigation tool designed to offer safer travel routes by avoiding crime hotspots in the Charlottesville area. It uses a dataset of historical crime incidents, including location, time, and type, to identify and cluster areas with higher crime rates using the k-means algorithm. These clusters then inform our routing system, developed with openrouteservice API, Leaflet, and Google Maps Geocaching, to provide users with paths that minimize their exposure to these high-risk areas, aiming for a safer journey.

# How we built it
We built Crime Compass by first collecting and preprocessing a comprehensive crime dataset to ensure accuracy and relevance. We then applied the k-means clustering algorithm to identify crime hotspots. These centroids were plotted on a map using the Leaflet, which also facilitated the creation of dynamic, user-friendly interfaces for route selection. To avoid the centroids, we utilized openrouteservice's APIs to calculate and display safer navigation routes that minimize exposure to these high-risk areas

# Challenges we ran into
One of the biggest issues was finding online documentation for openrouteservice, as it is significantly less used compared to Google Maps API or Bing Maps API. We chose to use go for this more niche tech stack as the other more commonly used ones did not allow for the robustness and scale we wanted for rerouting hotspots. This lack of online help led to an extensive amount of trial and error, but it was a great learning opportunity! I think we literally read every blog post concerning avoidPolygons haha. It was also the first time learning experience for a few of our members who had never worked with Django or Google Maps and of course openrouteservice. Another major challenge was accurately clustering crime data to reflect real-world conditions meaningfully.

# Accomplishments that we're proud of
Successfully integrating complex data analytics with user-friendly navigation interfaces was a significant achievement. Additionally, overcoming the technical challenges of utilizing many new tech stacks (django, openrouteservice, Google Maps Geocaching, keras) and learning to work as a cohesive team under pressure are accomplishments that have strengthened our resolve to continue improving Crime Compass. And of course, we are proud of developing a functional tool that can potentially make a difference in people's lives by enhancing their safety.

# What we learned
Through this project, we learned about some what was behind machine learning, especially in clustering and interpreting spatial data. Some of us learned how to work with a framework like django. All of us learned how to have a fun time coding together :D

# What's next for Crime Compass
Looking ahead, we plan to refine our algorithms for even more accurate crime hotspot detection and to expand our dataset to include real-time crime reports, we were able to start this but didn't have the time to fully integrate it. We also aim to introduce more personalized safety features, like alerting users about recent crimes in their vicinity or on their planned routes. Ultimately, we envision Crime Compass evolving into a comprehensive safety tool that incorporates user feedback and community safety initiatives to foster safer communities in places beyond just Charlottesville.
