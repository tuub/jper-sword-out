# JPER SWORDv2 Deposit Client

This document describes the process of carrying out SWORD deposits against repositories subscribed to the JPER
service.

Section numbers referenced here are as per the SWORDv2 profile here: http://swordapp.github.io/SWORDv2-Profile/SWORDProfile.html

The following operations are utilised

* 6.3.3. Creating a Resource with an Atom Entry
* 6.5.1. Replacing the File Content of a Resource
* 9.3. Completing a Previously Incomplete Deposit


## 6.3.3. Creating a Resource with an Atom Entry


    Client                   Interaction                 Server
    ------                   -----------                 ------
    
    Make metadata    ->      POST COL-IRI          ->    Ingest metadata.
    deposit                     + Auth                   Do not begin ingest workflow.
                                + Entry Doc             
                                In-Progress: True


    Record Failure    <-     4xx (Error)            <-   In case of error
    * Store error               XML Body
    * Update account
        record
                                                         
    Record Success    <-     200 (OK)               <-   On successful creation
    * Store receipt             XML Body


If the repository is configured to not return a deposit receipt, this will be followed up with an explicit
request for it

    Client                   Interaction                 Server
    ------                   -----------                 ------
    
    Request receipt    ->      GET Edit-IRI         ->   Get receipt
                                + Auth                   
                                                         
    Record Success     <-     200 (OK)              <-   
    * Store receipt             XML Body


## 6.5.1. Replacing the File Content of a Resource

    Client                   Interaction                 Server
    ------                   -----------                 ------
    
    Make content    ->      PUT EM-IRI          ->    Ingest package
    deposit                     + Auth                   Do not begin ingest workflow.
                                + Package
                                Packaging: [SimpleZip]

    Record Failure    <-     4xx (Error)            <-   In case of error
    * Store error               XML Body
    * Update account
        record
                                                         
    Record Success    <-     204 (No Content)       <-   On successful creation

## 9.3. Completing a Previously Incomplete Deposit

    Client                   Interaction                 Server
    ------                   -----------                 ------
    
    Make complete    ->      POST SE-IRI          ->    Trigger ingest workflow
    request                     + Auth                   
                                In Progress: False

    Record Failure    <-     4xx (Error)            <-   In case of error
    * Store error               XML Body
    * Update account
        record
                                                         
    Record Success    <-     204 (No Content)       <-   On successful completion