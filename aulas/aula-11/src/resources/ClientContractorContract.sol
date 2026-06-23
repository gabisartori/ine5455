pragma solidity ^0.8.0;

contract ClientContractorContract {

    address public owner;

    enum Status { Created, InEffect, SuccessfulTermination, UnsuccessfulTermination }
    enum ObligationStatus { Created, InEffect, Completed }

    Status public status;

    string public client;
    string public contractor;
    int public creationDate;

    // Store obligations and reference them by ID instead of relying on string comparison
    struct Obligation {
        string description;
        ObligationStatus status;
    }

    Obligation[] public obligations;

    constructor(
        string memory _client,
        string memory _contractor,
        int _creationDate
    ) {
        owner = msg.sender;
        client = _client;
        contractor = _contractor;
        creationDate = _creationDate;
        status = Status.Created;
    }

    function add_obligation(string memory obligation) public {
        obligations.push(
            Obligation({
                description: obligation,
                status: ObligationStatus.Created
            })
        );
    }

    function terminate() public {
        bool hasIncomplete = false;

        for (uint256 i = 0; i < obligations.length; i++) {
            if (obligations[i].status != ObligationStatus.Completed) {
                hasIncomplete = true;
                break;
            }
        }

        if (hasIncomplete) {
            status = Status.UnsuccessfulTermination;
        } else {
            status = Status.SuccessfulTermination;
        }
    }

    // SETTERS

    function activate() public {
        status = Status.InEffect;

        for (uint256 i = 0; i < obligations.length; i++) {
            obligations[i].status = ObligationStatus.InEffect;
        }
    }

    /// Mark an obligation as completed using its ID/index.
    function set_obligation_as_complete(string memory obligation) public {
        bytes32 obligationHash = keccak256(bytes(obligation));

        for (uint256 i = 0; i < obligations.length; i++) {
            if (
                keccak256(bytes(obligations[i].description)) == obligationHash
            ) {
                obligations[i].status = ObligationStatus.Completed;
                return;
            }
        }

        revert("Obligation not found");
    }

    // Optional helper getters

    function getObligationsCount() public view returns (uint256) {
        return obligations.length;
    }

    // GETTERS

    function obligations(uint256) public view returns (
        string memory description,
        ObligationStatus status
    );

    function getStatus() public view returns (Status) {
        return status;
    }

    function getClient() public view returns (string memory) {
        return client;
    }

    function getCreationDate() public view returns (int) {
        return creationDate;
    }

    function close() public pure returns (bool) {
        return true;
    }

    function is_created() public view returns (bool) {
        return status == Status.Created;
    }

    function is_in_effect() public view returns (bool) {
        return status == Status.InEffect;
    }

    function is_successful() public view returns (bool) {
        return status == Status.SuccessfulTermination;
    }

    function is_unsuccessful() public view returns (bool) {
        return status == Status.UnsuccessfulTermination;
    }
}