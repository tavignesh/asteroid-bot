module.exports = {
    name: 'clear-queue',
    aliases: ['cq'],
    category: 'Music',
    utilisation: '{prefix}clear-queue',

    execute(client, message) {
        if (!message.member.voice.channel) return message.channel.send(`${client.emotes.error} - Please Join a voice channel to Enjoy the music!`);

        if (message.guild.me.voice.channel && message.member.voice.channel.id !== message.guild.me.voice.channel.id) return message.channel.send(`${client.emotes.error} - I am already in a voice channel kindly join that one!`);

        if (!client.player.getQueue(message)) return message.channel.send(`${client.emotes.error} - No music being played!`);

        if (client.player.getQueue(message).tracks.length <= 1) return message.channel.send(`${client.emotes.error} - There is only one song in the queue.`);

        client.player.clearQueue(message);

        message.channel.send(`${client.emotes.success} - The queue has been succesfully **removed** !`);
    },
};