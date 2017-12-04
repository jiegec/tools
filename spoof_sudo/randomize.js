var sudo = require('sudo-prompt');
var options = {
  name: 'Spoof WiFi MAC Address'
};
sudo.exec('spoof randomize Wi-Fi', options,
  function(error, stdout, stderr) {
    if (error) throw error;
    console.log('stdout: ' + stdout);
  }
);
