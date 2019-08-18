const HDWalletProvider = require('truffle-hdwallet-provider');
const fs = require('fs');
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*"
    },
    naklechaConsortium: {
      network_id: "*",
      gas: 0,
      gasPrice: 0,
      provider: new HDWalletProvider(fs.readFileSync('mnemonic.env', 'utf-8'), "https://naklecha.blockchain.azure.com:3200/C7sLbEihlinGLsD2k9AXwVWH"),
      consortium_id: 1564473954588
    }
  },
  mocha: {},
};
