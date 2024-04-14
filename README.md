# website_content
testing deployment with content only website

## usage

initialise by fetching services dockerfiles with

```shell
run init
```
this will populate `./containers/dockerfiles` with the list from `./containers/seeds/seeds.yaml`

then build using astro-big-doc repo with

```shell
run build
```
this will take as input that will be mapped as volumes
- ./content
- ./public
- ./menu.yaml

and will generate the build in the `./dist` folder

then test by deploying a server on http://localhost
```shell
run server
```
