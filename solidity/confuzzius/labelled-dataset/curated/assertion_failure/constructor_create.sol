/*
 * @source: ChainSecurity
 * @author: Anton Permenev
 */

pragma solidity ^0.4.25;

contract ConstructorCreate{
    B b = new B();

    function check(){
        // <yes> <report> ASSERTION_FAILURE
        assert(b.foo() == 10);
    }

}

contract B{

    function foo() returns(uint){
        return 11;
    }
}
