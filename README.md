# Smart-Waste-Management

Smart Waste Management System: Sensor data is collected by Arduino Uno and published to
MQTT broker. The back end application written in Express.js subscribes to the data and stores
in a JSON file. AI planner codded in PDDL indicates the user when the threshold of the bin is
reached and closes the dustbin. A Notification is sent to the supervisor indicating the status of
the bin.
