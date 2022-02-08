import astroid
from astroid import nodes

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from pylint.lint import PyLinter

class PartitionColumnChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'test_'
    priority = -1
    msgs = {
        'W0001': (
            'Specify a partition column parameter for <reason>',
            'no-partition-column',
            'Specify a partition column parameter.'
        ),
    }
    options = (
        (
            'ignore-ints',
            {
                'default': False, 'type': 'yn', 'metavar' : '<y or n>',
                'help': 'Allow returning non-unique integers',
            }
        ),
    )

    def visit_assign(self, node: nodes.Assign) -> None:
        """Called when a :class:`.nodes.Call` node is visited.
        See :mod:`astroid` for the description of available nodes.
        """
        # if not (
        #     isinstance(node.func, nodes.Attribute)
        #     and isinstance(node.func.expr, nodes.Name)
        #     and node.func.expr.name == self.config.store_locals_indicator
        #     and node.func.attrname == "create"
        # ):
        print(node.value)
        ok = True
        in_class = node.frame(future=True)
        # Can't really figure out how to get the HiveDSConfig part to work since the Name object for some reason doesn't
        # expose the attributes in the documentation
        for keyword in node.value.keywords:
            # Param name
            if keyword.arg == 'batch_ds_config':
                # If there is a batch ds config param check if datetime_partition is in the params
                # Not super right but is a super jank implementation that somewhat works
                ok = False
                for params in keyword.value.keywords:
                    if params.arg == 'datetime_partition_columns':
                        ok = True
        print(ok)
        # for param in node.keywords:
        #     print(param.name)


def register(linter):
    """required method to auto register this checker"""
    print("stuffs")
    linter.register_checker(PartitionColumnChecker(linter))