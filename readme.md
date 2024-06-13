# CIE A/L IT (9626) - Crash Course - Resources Website

My journey doing the CIE Advanced Level - Information Technology (9626) syllabus in 3 months.

## Deploying

After every push to the `master` branch, github-pages will build and deploy it.

## Testing Locally

### Windows

- Download and install [Ruby (with Devkit)](https://rubyinstaller.org/downloads/). Run `ruby -v` in the command-line to verify installation.

- Install [Bundler](https://bundler.io/).

  ```
  gem install bundler
  ```

  - Update Bundler:

    ```
    bundle update --bundler
    ```

- Come to the current working directory

- Backup already existing `Gemfile.lock` if it exists

  ```
  rename Gemfile.lock Gemfile.lock.bak
  ```

- Install dependencies:

  ```
  bundle install --verbose
  ```

  - Clear cache and install

    ```
    bundle clean --force
    bundle install
    ```

- Start serving:

  ```
  bundle exec jekyll serve
  ```

## Updating Font Awesome

1. Go to <https://icomoon.io/app/>
2. Choose Import Icons and load `icomoon-selection.json`
3. Choose Generate Font → Download
4. Copy the font files and adapt the CSS to the paths we use in Jekyll
