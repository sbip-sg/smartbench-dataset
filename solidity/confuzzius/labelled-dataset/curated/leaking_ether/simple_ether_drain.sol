pragma solidity ^0.4.22;

// <yes> <report> LEAKING_ETHER
contract SimpleEtherDrain {

  function withdrawAllAnyone() {
    msg.sender.transfer(this.balance);
  }

  function () public payable {
  }

}
