// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract BugSample{
    address owner;
    constructor (){
        owner = msg.sender;
    }

    function overflow_uint8(uint8 x) public returns (uint8){
        return x + 1; // NUMERIC_TRUNCATION (Overflow of uint8)
    }

    modifier onlyOwner() {
        // require(msg.sender == owner, "Ownable: caller is not the owner");
        // comment out which means there is no check and the bug is not fixed
        _;
    }
    function unprotected_bug() public onlyOwner{
        selfdestruct(msg.sender); // UNPROTECTED_SELFDESTRUCT
    }
    function wrong_unprotected_bug() public {
        revert(); // will never get pass this point
        selfdestruct(msg.sender); // UNPROTECTED_SELFDESTRUCT
    }
    function bug_integer( uint a , uint b ) public returns ( uint ) {
        return a + b ;
    }
    function wrong_integer_bug(uint a, uint b) public returns (uint) {
        require (a + b >= a);
        return a + b;
    }
    function get_access() public{
        owner = msg.sender;
    }

}
