const Discord = require('discord.js')


module.exports={
  async play(message, url, radio){
    const VC = message.member.voice.channel;
     VC.join()
        .then(connection =>  {
            const dispatcher = connection.play(url);
          
            dispatcher.on("end", end => {VC.leave()});
        })
        .catch(console.error);

        const emb = new Discord.MessageEmbed()
            emb.setTitle(radio)
            emb.setColor('RANDOM')
            emb.setImage('https://s8.gifyu.com/images/giphy582f10e0bc9a8822.gif')
            emb.setDescription('Started playing'+ radio)
            emb.setFooter('Loney V3.5')
            try{
          var playingMessage =  await message.channel.send(emb);
       await playingMessage.react(":stop_button:");
    
    } catch (error) {
      console.error(error);
    }

    const filter = (reaction, user) => user.id !== message.client.user.id;
    var collector = playingMessage.createReactionCollector(filter);

    collector.on("collect", (reaction, user) => {
      const member = message.guild.member(user);

      switch (reaction.emoji.name) {
        case ":stop_button:":
        VC.leave()
        playingMessage.reactions.removeAll().catch(console.error);
      playingMessage.delete({ timeout: 3000 }).catch(console.error);
          break;


        default:
          reaction.users.remove(user).catch(console.error);
          break;
      }
    });

    collector.on("end", () => {
      
    });
  }
}
