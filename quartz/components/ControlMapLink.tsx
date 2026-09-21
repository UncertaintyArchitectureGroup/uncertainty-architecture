import { QuartzComponentConstructor } from "./types"
import { FullSlug, resolveRelative } from "../util/path"

export default (() =>
  ({ fileData }) =>
    process.env.UA_INCLUDE_DRAFTS === "1" ? null : (
      <a
        class="control-map-link"
        data-router-ignore="true"
        href={resolveRelative(fileData.slug!, "control-map/index" as FullSlug)}
      >
        Repository Control Map ↗
      </a>
    )) satisfies QuartzComponentConstructor
