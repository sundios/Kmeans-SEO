# SEO - Grouping URLs with Kmeans clustering to see important insights of your site

In this project I will show step by step how to use Google search Console data and Kmeans clustering to group your URLs depending on a specific KPI. With this you will be able to see some important insights and optimize better your site. It will also give you an overview of the site from a more analitical stand point and will help you to make data driven decisions.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To be able to use this you will need the following Prerequisites

```
Python3
Google search console Access
Screaming Frog

```

### Getting the Data from GSC

The first step we need is to get access to [Google Search Console](https://search.google.com/search-console) for your own site.
Once in the console we need to go to Performance and export page a report that includes the following.


| URL | Clicks	| Impressions |CTR	| Position| 
| ----| ------- | ------------| ----| --------|

You can select the time frame that you want and add the necessary filterst that you think they are right for your project.
If you want to get more data(more thn 1,000 URLs) You can try using the Google Search Console APi to make bigger requests.

## Getting Title and description Lenghts

Once we have the list URLs, we go to screaming frog and in mode we select list and drop our list manually.

Here we would only need to export the title lengths and the description lengths. Once we get the length we can do a Vlookup and add it to our Google Search Console export we did before, the spreadsheet shoudl look like this:

| URL | Title Length | Description Length | Clicks	| Impressions |CTR	| Position| 
| ----| ------------ |------------------- | --------| ------------| ----|-------- |

### Installing Python Libraries

now that we have our dataset ready, we need to install some libraries that we will be suing for this.
To install the libraries copy the following and run it in the terminal

```
pip install pandas
pip install numpy
pip install sklearn
pip install matplotlib
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

