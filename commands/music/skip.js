module.exports = {
    name: 'skip',
    aliases: ['sk'],
    category: 'Music',
    utilisation: '{prefix}skip',

    execute(client, message) {
        if (!message.member.voice.channel) return message.channel.send(`${client.emotes.error} - Please Join a voice channel to Enjoy the music!`);

        if (message.guild.me.voice.channel && message.member.voice.channel.id !== message.guild.me.voice.channel.id) return message.channel.send(`${client.emotes.error} - I am already in a voice channel kindly join that one!`);

        if (!client.player.getQueue(message)) return message.channel.send(`${client.emotes.error} - No music currently playing !`);

        const success = client.player.skip(message);

        if (success) message.channel.send(`${client.emotes.success} - The current music has just been **skipped** !`);
    },
};