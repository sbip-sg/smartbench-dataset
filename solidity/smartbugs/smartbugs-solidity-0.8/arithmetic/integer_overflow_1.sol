/*
 * @source: https://github.com/trailofbits/not-so-smart-contracts/blob/master/integer_overflow/integer_overflow_1.sol
 * @author: -
 * @vulnerable_at_lines: 14
 */

 pragma solidity ^0.4.15;

 contract Overflow {
     uint private sellerBalance=0;

     function foo(uint value) public returns (bool){
       // <yes> <report> ARITHMETIC
       sellerBalance += value; // possible overflow
       // possible auditor assert
       // assert(sellerBalance >= value);
       return true;
     }

     function add(uint value, address addr) public returns (bool){
         // <yes> <report> ARITHMETIC
         sellerBalance += value; // possible overflow
         bool bar = foo(value);

         // possible auditor assert
         // assert(sellerBalance >= value);
         return true;
     }

  // function safe_add(uint value) returns (bool){
  //   require(value + sellerBalance >= sellerBalance);
  // sellerBalance += value;
  // }
 }
