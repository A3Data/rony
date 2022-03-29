# Recursive function to install module ant its dependencies
install_module()
{
    d="../../rony/module_templates/$1/"
    # Extracting module name from module path
    module_name=$(basename "$d")
    # Module json file path
    json_path=$(echo $d | sed 's|/$|.json|')

    echo "$module_name"
    jq -c '.dependencies|.[]' $json_path | while read i; do
        dep_name=$(echo  $i | sed 's/"//g')
        echo dep_name
        install_module "$dep_name"
    done

   rony add-module $module_name -y
}
