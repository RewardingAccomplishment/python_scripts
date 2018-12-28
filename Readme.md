# Project Title

Small python scripts for debugging, logging, simple one-file applications. 

#Scripts List
build.py        Script for Test Driven Development
                script make in loop ceedling test, it allows TDD with ceedling
                for make compatible with python 3.x
tdd_cmd.py      File contain class that invoke ceedling test in infinite loop.
                File required for build.py script.


## Getting Started

Make install and follow the manual:

### Prerequisites


### Installing

Step for installing:
* [Ceedling](http://www.throwtheswitch.org/ceedling/) - The framework used
   + gem install ceedling
* Download repo and follow the manual:
   + Install python3: sudo apt-get install python3
   + Install pip3: sudo pip3 install urwid
   + Install urwid package: pip3 install urwid   

## Running the tests

New project:
Run ./build.py script then Files -> New Project -> (type the project name) -> arrow down -> press enter to confirm.

Console output:
 > $ ./build.py 
 > Welcome to Ceedling!
 >       create  demo/vendor/ceedling/docs/CeedlingPacket.md
 >       create  demo/vendor/ceedling/docs/CException.md
 >       create  demo/vendor/ceedling/docs/CMock_Summary.md
 > ...
 >    create  demo/vendor/ceedling/vendor/unity/src/unity_internals.h
 >       create  demo/project.yml
 >       create  demo/ceedling
 > 
 > Project 'demo' created!
 >  - Tool documentation is located in vendor/ceedling/docs
 >  - Execute 'ceedling help' to view available test & build tasks

New module: 
Please go to the created project _project_name_ and run _path_to_script_/build.py.
Then Files -> New Module -> (type the module name) -> arrow down -> press enter to confirm.

Console output:
 > $cd demo/
 > $../build.py 
 > File src/TestModule.c created
 > File src/TestModule.h created
 > File test/test_TestModule.c created
 > Generate Complete

Check:
Run ./build.py script then Files -> New Project -> (type the project name) -> arrow down -> press enter to confirm.

Console output:
 > $ ../build.py 
 > Starting test:all
 > wait for boost or exit
 > 
 > 
 > Test 'test_NewModulee.c'
 > ------------------------
 > Generating runner for test_NewModulee.c...
 > Compiling test_NewModulee_runner.c...
 > Compiling test_NewModulee.c...
 > Compiling unity.c...
 > Compiling NewModulee.c...
 > Compiling cmock.c...
 > Linking test_NewModulee.out...
 > Running test_NewModulee.out...
 > 
 > 
 > Test 'test_TestModule.c'
 > ------------------------
 > Generating runner for test_TestModule.c...
 > Compiling test_TestModule_runner.c...
 > Compiling test_TestModule.c...
 > Compiling TestModule.c...
 > Linking test_TestModule.out...
 > Running test_TestModule.out...
 > 
 > --------------------
 > IGNORED TEST SUMMARY
 > --------------------
 > [test_NewModulee.c]
 >   Test: test_NewModulee_NeedToImplement
 >   At line (14): "Need to Implement NewModulee"
 > 
 > [test_TestModule.c]
 >   Test: test_TestModule_NeedToImplement
 >   At line (14): "Need to Implement TestModule"
 > 
 > --------------------
 > OVERALL TEST SUMMARY
 > --------------------
 > TESTED:  2
 > PASSED:  0
 > FAILED:  0
 > IGNORED: 2
 > 
 > <-------->|<- delay time
 > ----------
 > 
 > Test 'test_NewModulee.c'
 > ------------------------
 > Running test_NewModulee.out...
 > 
 > 
 > Test 'test_TestModule.c'
 > ------------------------
 > Running test_TestModule.out...
 > 
 > --------------------
 > IGNORED TEST SUMMARY
 > --------------------
 > [test_NewModulee.c]
 >   Test: test_NewModulee_NeedToImplement
 >   At line (14): "Need to Implement NewModulee"
 > 
 > [test_TestModule.c]
 >   Test: test_TestModule_NeedToImplement
 >   At line (14): "Need to Implement TestModule"
 > 
 > --------------------
 > OVERALL TEST SUMMARY
 > --------------------
 > TESTED:  2
 > PASSED:  0
 > FAILED:  0
 > IGNORED: 2
 > 
 > <-------->|<- delay time
 > ----------
 > 
 > Test 'test_NewModulee.c'
 > ------------------------
 > Running test_NewModulee.out...
 > 
 > 
 > Test 'test_TestModule.c'
 > ------------------------
 > Running test_TestModule.out...
 > 
 > --------------------
 > IGNORED TEST SUMMARY
 > --------------------
 > [test_NewModulee.c]
 >   Test: test_NewModulee_NeedToImplement
 >   At line (14): "Need to Implement NewModulee"
 > 
 > [test_TestModule.c]
 >   Test: test_TestModule_NeedToImplement
 >   At line (14): "Need to Implement TestModule"
 > 
 > --------------------
 > OVERALL TEST SUMMARY
 > --------------------
 > TESTED:  2
 > PASSED:  0
 > FAILED:  0
 > IGNORED: 2
 > 
 > <-------->|<- delay time
 > ----------
 > 
 > Test 'test_NewModulee.c'
 > ------------------------
 > Running test_NewModulee.out...
 > 
 > 
 > Test 'test_TestModule.c'
 > ------------------------
 > Running test_TestModule.out...
 > 
 > --------------------
 > IGNORED TEST SUMMARY
 > --------------------
 > [test_NewModulee.c]
 >   Test: test_NewModulee_NeedToImplement
 >   At line (14): "Need to Implement NewModulee"
 > 
 > [test_TestModule.c]
 >   Test: test_TestModule_NeedToImplement
 >   At line (14): "Need to Implement TestModule"
 > 
 > --------------------
 > OVERALL TEST SUMMARY
 > --------------------
 > TESTED:  2
 > PASSED:  0
 > FAILED:  0
 > IGNORED: 2
 > 
 > <-------->|<- delay time
 > -------q
 > 

### Break down into end to end tests

TODO

### And coding style tests

TODO

## Deployment

TODO

## Built With

TODO

## Contributing

TODO

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

## License

Please read [LICENSE.md]() for details on our code of conduct, and the process for submitting pull requests to us.

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](https://github.com/RewardingAccomplishment/python_scripts/blob/master/LICENSE) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

