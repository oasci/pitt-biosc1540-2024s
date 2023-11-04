<h1 align="center">Computational Biology</h1>

<h3 align="center">BIOSC 1540</h3>

<p align="center">
    Spring 2024 •
    <a href="https://www.pitt.edu/">University of Pittsburgh</a> •
    <a href="https://www.biology.pitt.edu/">Department of Biological Sciences</a>
</p>

## Encryption

[git-secret](https://github.com/sobolevn/git-secret) is used to encrypt course materials that are in preparation.
Use [`git secret add`](https://sobolevn.me/git-secret/git-secret-add) to encrypt an untracked file.
This will add a line to `.gitignore` and `.gitsecret/paths/mapping.cfg` to mark that it should be a `.secret` file.
To stop encrypting the file, remove the lines in `.gitignore` and `.gitsecret/paths/mapping.cfg` and delete the `.secret` file.

[pre-commit](https://pre-commit.com/) hooks are used to ensure all desired files are encrypted before commits.
Building the book before committing is beneficial as it will encrypt and decrypt files as necessary so you can see which files are changing.
`git secret reveal` will allow you to decrypt these files if you have access.

## License

Code contained in this project is released under the [MIT License](https://spdx.org/licenses/MIT.html) as specified in [`LICENSE_CODE`][license-code].
This license grants you the freedom to use, modify, and distribute it as long as you include the original copyright notice contained in [`LICENSE_CODE`][license-code] and the following notice.

> Portions of this code were incorporated and adapted with permission from [BIOSC 1540 at Pitt](https://github.com/oasci/pitt-biosc-1540-2024-spring) by OASCI under the [MIT License](https://github.com/oasci/pitt-biosc-1540-2024-spring/blob/main/LICENSE_code.md).

All other data, information, documentation, and associated content provided within this project are released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) as specified in [`LICENSE_INFO`][license-info].
This means you are free to share and adapt the non-code elements, but you must include the following notice.

> Portions of this project were incorporated and adapted with permission from [BIOSC 1540 at Pitt](https://github.com/oasci/pitt-biosc-1540-2024-spring) by OASCI under the [CC BY 4.0 License](https://github.com/oasci/pitt-biosc-1540-2024-spring/blob/main/LICENSE_INFO.md).

[license-code]: https://github.com/oasci/pitt-biosc-1540-2024-spring/blob/main/LICENSE_CODE.md
[license-info]: https://github.com/oasci/pitt-biosc-1540-2024-spring/blob/main/LICENSE_INFO.md
