pragma solidity ^0.4.22;


contract SimpleEtherDrain {

  function withdrawAllAnyone() {
    // <yes> <report> LEAKING_ETHER
    msg.sender.transfer(this.balance);
  }

  function () public payable {
  }

}
