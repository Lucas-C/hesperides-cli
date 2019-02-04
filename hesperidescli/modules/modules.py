import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("create-module")
@click.option("--from-module-name")
@click.option("--from-module-version")
@click.option("--from-is-working-copy", is_flag=True)
@click.option("--body")
def create_module(from_module_name, from_module_version, from_is_working_copy, body):
    params = {}
    if from_module_name is None and from_module_version:
        print("--from-module-name required when --from-module-version is given")
        raise click.Abort()
    if from_module_name and from_module_version is None:
        print("--from-module-version required when --from-module-name is given")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    if from_module_name:
        params["from_module_name"] = from_module_name
    if from_module_version:
        params["from_module_version"] = from_module_version
    if from_is_working_copy:
        params["from_is_working_copy"] = from_is_working_copy
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post("/rest/modules", params=params, body=file_body)
    utils.pretty_print(response)


@click.command("create-module-release")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--release-version")
def create_module_release(module_name, module_version, release_version):
    params = {}
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    params["module_name"] = module_name
    params["release_version"] = release_version
    response = Client().post("/rest/modules/create_release", params=params)
    utils.pretty_print(response)


@click.command("delete-module-workingcopy-template")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--body")
def create_module_workingcopy_template(module_name, module_version, body):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post(
        "/rest/rest/modules" + module_name + "/" + module_version + "/workingcopy",
        body=file_body,
    )
    utils.pretty_print(response)


@click.command("delete-module-release")
@click.option("--module-name")
@click.option("--module-version")
def delete_module_release(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    response = Client().delete(
        "/rest/rest/modules" + module_name + "/" + module_version + "/release"
    )
    utils.pretty_print(response)


@click.command("delete-module-workingcopy")
@click.option("--module-name")
@click.option("--module-version")
def delete_module_workingcopy(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    response = Client().delete(
        "/rest/rest/modules" + module_name + "/" + module_version + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("delete-module-workingcopy-template")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--template-name")
def delete_module_workingcopy_template(module_name, module_version, template_name):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    response = Client().delete(
        "/rest/rest/modules"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-module")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--module-type")
def get_module(module_name, module_version, module_type):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_type and module_version is None:
        print("--module-version required")
        raise click.Abort()
    client = Client()
    if module_version is None and module_type is None:
        response = client.get("/rest/modules/" + module_name)
        utils.pretty_print(response)
    if module_version and module_type is None:
        response = client.get("/rest/modules/" + module_name + "/" + module_version)
        utils.pretty_print(response)
    if module_version and module_type:
        response = client.get(
            "/rest/modules/" + module_name + "/" + module_version + "/" + module_type
        )
        utils.pretty_print(response)


@click.command("get-module-release")
@click.option("--module-name")
@click.option("--module-version")
def get_module_release(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    response = Client().get(
        "/rest/modules/" + module_name + "/" + module_version + "/release"
    )
    utils.pretty_print(response)


@click.command("get-module-release-template")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--template-name")
def get_module_release_template(module_name, module_version, template_name):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    response = Client().get(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/release/templates"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-module-release-templates")
@click.option("--module-name")
@click.option("--module-version")
def get_module_release_templates(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    response = Client().get(
        "/rest/modules/" + module_name + "/" + module_version + "/release/templates"
    )
    utils.pretty_print(response)


@click.command("get-module-workingcopy")
@click.option("--module-name")
@click.option("--module-version")
def get_module_workingcopy(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    response = Client().get(
        "/rest/modules/" + module_name + "/" + module_version + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("get-module-workingcopy-template")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--template-name")
def get_module_workingcopy_template(module_name, module_version, template_name):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    response = Client().get(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-module-workingcopy-templates")
@click.option("--module-name")
@click.option("--module-version")
def get_module_workingcopy_templates(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    response = Client().get(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates/"
    )
    utils.pretty_print(response)


@click.command("get-modules")
def get_modules():
    response = Client().get("/rest/modules/")
    utils.pretty_print(response)


@click.command("perform-search-modules")
@click.option("--terms")
def perform_search_modules(terms):
    params = {}
    if terms is None:
        print("--terms required")
        raise click.Abort()
    params["terms"] = terms
    response = Client().post("/rest/modules/perform_search", params=params)
    utils.pretty_print(response)


@click.command("search-module")
@click.option("--terms")
def search_module(terms):
    params = {}
    if terms is None:
        print("--terms required")
        raise click.Abort()
    params["temrs"] = terms
    response = Client().post("/rest/modules/search", params=params)
    utils.pretty_print(response)


@click.command("update-module")
@click.option("--body")
def update_module(body):
    if body is None:
        print("--body required")
        raise click.Abort()
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().put("/rest/modules/", body=file_body)
    utils.pretty_print(response)


@click.command("update-module-workingcopy-template")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--body")
def update_module_workingcopy_template(module_name, module_version, body):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().put(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates",
        body=file_body,
    )
    utils.pretty_print(response)
