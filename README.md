# Python Experiments 2

Repository to store data and scripts relate to Python programs experiments.

This programs have some test sets previous developed by their creators. Each project has a `0-ts` directory containing these previous generated test sets.


## Pynguin

For two programs we have to limit the number of iteractions to 2200. If we leave the tool running for 600 seconds it causes an execution error and finishes before to generate the test set.

This happens for programs binarySearchTree3 and sort1.

In this case, we run `pynguin` as follows:

```
pynguin --project-path ./ --output-path ./RANDOM --module-name binarySearchTree3 -v --create-coverage-report True --algorithm=RANDOM --seed 1234 --maximum-search-time 600 --maximum_iterations 2200
```


## CosmicRay

We have to set up Timeout limit to RANDOM tests to 60s instead the default value (20s). For the majority of programs the `cosmic-ray --verbosity INFO baseline` command finished with TIMEOUT error with timeout default value.
