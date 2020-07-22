
const sendData = (event) =>{
  event.preventDefault()
  let validated = validateData()

  if (validated === true){
    document.getElementById('champion-form').submit()
  }
  else if(validated === false){
    console.log('not valid')
  }
}

let championsNormalized = [ 'AATROX', 'AHRI','AKALI',  'ALISTAR','AMUMU',  'ANIVIA', 'ANNIE','APHELIOS','ASHE','AURELIONSOL','AZIR','BARD','BLITZCRANK','BRAND','BRAUM','CAITLYN','CAMILLE','CASSIOPEIA','CHO\'GATH','CORKI','DARIUS','DIANA','DR.MUNDO','DRAVEN','EKKO','ELISE','EVELYNN','EZREAL','FIDDLESTICKS','FIORA','FIZZ','GALIO','GANGPLANK','GAREN','GNAR','GRAGAS','GRAVES','HECARIM','HEIMERDINGER','ILLAOI','IRELIA','IVERN','JANNA','JARVANIV','JAX','JAYCE','JHIN','JINX','KAI\'SA','KALISTA','KARMA','KARTHUS','KASSADIN','KATARINA','KAYLE','KAYN','KENNEN','KHA\'ZIX','KINDRED','KLED','KOG\'MAW','LEBLANC','LEESIN','LEONA','LISSANDRA','LUCIAN','LULU','LUX','MALPHITE','MALZAHAR','MAOKAI','MASTERYI','MISSFORTUNE','MORDEKAISER','MORGANA','NAMI','NASUS','NAUTILUS','NEEKO','NIDALEE','NOCTURNE','NUNUANDWILLUMP','OLAF','ORIANNA','ORNN','PANTHEON','POPPY','PYKE','QIYANA','QUINN','RAKAN','RAMMUS','REK\'SAI','RENEKTON','RENGAR','RIVEN','RUMBLE','RYZE','SEJUANI','SENNA','SETT','SHACO','SHEN','SHYVANA','SINGED','SION','SIVIR','SKARNER','SONA','SORAKA','SWAIN','SYLAS','SYNDRA','TAHMKENCH','TALIYAH','TALON','TARIC','TEEMO','THRESH','TRISTANA','TRUNDLE','TRYNDAMERE','TWISTEDFATE','TWITCH','UDYR','URGOT','VARUS','VAYNE','VEIGAR','VEL\'KOZ','VI','VIKTOR','VLADIMIR','VOLIBEAR','WARWICK','WUKONG','XAYAH','XERATH','XINZHAO','YASUO','YORICK','YUUMI','ZAC','ZED','ZIGGS','ZILEAN','ZOE','ZYRA' ]
const validateData = () =>{

  let championEntered = document.getElementById('champion-name-input').value

  let normalizedChampionEntered = championEntered.split(" ").join("").toUpperCase()
  console.log(normalizedChampionEntered)
  console.log(typeof(normalizedChampionEntered))
  for(let i = 0; i < championsNormalized.length; i++ ){
    if(normalizedChampionEntered == championsNormalized[i]){
      return true
    }
  }
  return false
}

//can press enter to activate the button
// Get the input field
var input = document.getElementById("champion-name-input");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("submit-button").click();
  }
});

document.getElementById('submit-button').addEventListener('click',sendData)

