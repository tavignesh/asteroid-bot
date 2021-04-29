module.exports = {
    name: 'loop',
    aliases: ['lp', 'repeat'],
    category: 'Music',
    utilisation: '{prefix}loop',

    execute(client, message, args) {
        if (!message.member.voice.channel) return message.channel.send(`${client.emotes.error} - Please Join a voice channel to Enjoy the music!`);

        if (message.guild.me.voice.channel && message.member.voice.channel.id !== message.guild.me.voice.channel.id) return message.channel.send(`${client.emotes.error} - I am already in a voice channel kindly join that one!`);

        if (!client.player.getQueue(message)) return message.channel.send(`${client.emotes.error} - No music currently playing !`);

        if (args.join(" ").toLowerCase() === 'queue') {
            if (client.player.getQueue(message).loopMode) {
                client.player.setLoopMode(message, false);
                return message.channel.send(`${client.emotes.success} - Repeat mode is **disabled** !`);
            } else {
                client.player.setLoopMode(message, true);
                return message.channel.send(`${client.emotes.success} - Repeat mode is **enabled** the whole queue will be repeated endlessly !`);
            };
        } else {
            if (client.player.getQueue(message).repeatMode) {
                client.player.setRepeatMode(message, false);
                return message.channel.send(`${client.emotes.success} - Repeat mode is **disabled** !`);
            } else {
                client.player.setRepeatMode(message, true);
                return message.channel.send(`${client.emotes.success} - Repeat mode is **enabled** the current music will be repeated endlessly !`);
            };
        };
    },
};